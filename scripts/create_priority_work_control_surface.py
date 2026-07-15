from __future__ import annotations

import math
import random
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "3d"
BLEND_PATH = OUT_DIR / "priority-work-control-surface.blend"
GLB_PATH = OUT_DIR / "priority-work-control-surface.glb"
PREVIEW_PATH = OUT_DIR / "priority-work-control-surface-preview.png"


COLORS = {
    "currant": (0.009, 0.012, 0.055, 1.0),
    "currant_lift": (0.03, 0.04, 0.16, 1.0),
    "panel": (0.055, 0.065, 0.21, 1.0),
    "panel_edge": (0.16, 0.22, 0.36, 1.0),
    "white": (0.92, 0.94, 0.97, 1.0),
    "muted": (0.54, 0.61, 0.70, 1.0),
    "emerald": (0.0, 0.40, 0.28, 1.0),
    "forest": (0.37, 0.74, 0.36, 1.0),
    "tangerine": (0.98, 0.65, 0.09, 1.0),
    "line_blue": (0.16, 0.34, 0.62, 1.0),
}


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 180


def make_mat(
    name: str,
    color: tuple[float, float, float, float],
    *,
    roughness: float = 0.55,
    metallic: float = 0.0,
    emission: tuple[float, float, float, float] | None = None,
    emission_strength: float = 0.0,
) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if emission:
            bsdf.inputs["Emission Color"].default_value = emission
            bsdf.inputs["Emission Strength"].default_value = emission_strength
    return mat


def add_box(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    mat: bpy.types.Material,
    *,
    bevel: float = 0.035,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    if bevel:
        bevel_mod = obj.modifiers.new(f"{name}_soft_edges", "BEVEL")
        bevel_mod.width = bevel
        bevel_mod.segments = 3
        bevel_mod.affect = "EDGES"
        obj.modifiers.new(f"{name}_weighted_normals", "WEIGHTED_NORMAL")
    return obj


def add_cylinder(
    name: str,
    location: tuple[float, float, float],
    radius: float,
    depth: float,
    mat: bpy.types.Material,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=radius, depth=depth, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    obj.modifiers.new(f"{name}_weighted_normals", "WEIGHTED_NORMAL")
    return obj


def add_sphere(
    name: str,
    location: tuple[float, float, float],
    radius: float,
    mat: bpy.types.Material,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=radius, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def add_line(
    name: str,
    points: list[tuple[float, float, float]],
    mat: bpy.types.Material,
    *,
    bevel_depth: float = 0.014,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 16
    curve.bevel_depth = bevel_depth
    curve.bevel_resolution = 3
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, coords in zip(spline.points, points):
        point.co = (coords[0], coords[1], coords[2], 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    return obj


def add_label(
    name: str,
    text: str,
    location: tuple[float, float, float],
    size: float,
    mat: bpy.types.Material,
    *,
    rotation_z: float = 0.0,
) -> bpy.types.Object:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(72), 0, rotation_z))
    obj = bpy.context.object
    obj.name = name
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.materials.append(mat)
    return obj


def animate_pulse(obj: bpy.types.Object, start: Vector, end: Vector, first_frame: int) -> None:
    obj.location = start
    obj.keyframe_insert(data_path="location", frame=first_frame)
    obj.location = end
    obj.keyframe_insert(data_path="location", frame=first_frame + 95)
    obj.location = start
    obj.keyframe_insert(data_path="location", frame=first_frame + 180)
    if obj.animation_data and obj.animation_data.action:
        for fcurve in obj.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = "SINE"


def build_scene() -> None:
    clear_scene()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    random.seed(7)

    mats = {
        "background": make_mat("currant field", COLORS["currant"], roughness=0.8),
        "base": make_mat("raised dark operating surface", COLORS["currant_lift"], roughness=0.7),
        "panel": make_mat("work surface panels", COLORS["panel"], roughness=0.58),
        "edge": make_mat(
            "muted panel edge",
            COLORS["panel_edge"],
            roughness=0.5,
            emission=COLORS["line_blue"],
            emission_strength=0.05,
        ),
        "white": make_mat("soft white type", COLORS["white"], roughness=0.55),
        "muted": make_mat("muted work fragments", COLORS["muted"], roughness=0.65),
        "emerald": make_mat(
            "governed emerald signal",
            COLORS["emerald"],
            roughness=0.35,
            emission=COLORS["emerald"],
            emission_strength=0.45,
        ),
        "forest": make_mat(
            "active forest pulse",
            COLORS["forest"],
            roughness=0.25,
            emission=COLORS["forest"],
            emission_strength=1.8,
        ),
        "tangerine": make_mat(
            "priority tangerine signal",
            COLORS["tangerine"],
            roughness=0.35,
            emission=COLORS["tangerine"],
            emission_strength=0.65,
        ),
        "line": make_mat(
            "thin blue flow lines",
            COLORS["line_blue"],
            roughness=0.45,
            emission=COLORS["line_blue"],
            emission_strength=0.75,
        ),
    }

    # Environment and operating surface.
    add_box("deep background field", (0, 0, -0.18), (17.5, 9.0, 0.08), mats["background"], bevel=0)
    add_box("low operating table", (0.4, 0, 0), (14.4, 5.5, 0.12), mats["base"], bevel=0.08)

    # Subtle longitudinal work lanes.
    lane_ys = [-1.85, -1.12, -0.38, 0.38, 1.12, 1.85]
    for idx, y in enumerate(lane_ys):
        add_box(f"execution lane {idx + 1}", (0.3, y, 0.09), (11.2, 0.055, 0.035), mats["edge"], bevel=0.02)

    # Fragmented inputs on the left.
    for idx in range(18):
        x = random.uniform(-6.4, -4.2)
        y = random.uniform(-2.2, 2.2)
        z = 0.18 + random.uniform(0, 0.12)
        w = random.uniform(0.28, 0.62)
        h = random.uniform(0.16, 0.36)
        mat = mats["muted"] if idx % 5 else mats["tangerine"]
        obj = add_box(f"ambiguous input fragment {idx + 1}", (x, y, z), (w, h, 0.05), mat, bevel=0.025)
        obj.rotation_euler[2] = random.uniform(-0.35, 0.35)

    # Central governed delivery grid.
    for col, x in enumerate([-2.4, -1.3, -0.2, 0.9, 2.0]):
        add_box(f"delivery gate column {col + 1}", (x, 0, 0.17), (0.055, 4.55, 0.12), mats["edge"], bevel=0.018)

    for idx, x in enumerate([-2.4, -1.3, -0.2, 0.9, 2.0]):
        for lane, y in enumerate(lane_ys):
            if (idx + lane) % 2 == 0:
                node_mat = mats["emerald"] if idx in [1, 3] else mats["panel"]
                add_cylinder(f"governance node {idx + 1}-{lane + 1}", (x, y, 0.32), 0.085, 0.08, node_mat)

    # Output proof panels on the right.
    output_specs = [
        ("owner proof panel", "OWNER", 4.25, 1.28, mats["forest"]),
        ("metric proof panel", "METRIC", 4.9, 0.0, mats["tangerine"]),
        ("workflow proof panel", "WORKFLOW", 4.25, -1.28, mats["forest"]),
    ]
    for name, label, x, y, accent in output_specs:
        add_box(name, (x, y, 0.34), (1.42, 0.78, 0.12), mats["panel"], bevel=0.05)
        add_box(f"{name} accent", (x - 0.56, y, 0.43), (0.05, 0.52, 0.045), accent, bevel=0.016)
        for i, height in enumerate([0.16, 0.28, 0.41]):
            add_box(
                f"{name} bar {i + 1}",
                (x - 0.18 + i * 0.22, y - 0.18 + height / 2, 0.46),
                (0.09, height, 0.035),
                accent if i == 2 else mats["muted"],
                bevel=0.01,
            )
        add_label(f"{name} label", label, (x + 0.14, y + 0.26, 0.50), 0.115, mats["white"])

    # Flow paths from ambiguity through the delivery layer to proof.
    path_sets = [
        [(-5.9, -1.9, 0.37), (-3.4, -1.7, 0.38), (-1.3, -1.12, 0.42), (1.2, -1.12, 0.42), (3.55, -1.28, 0.49)],
        [(-6.1, -0.4, 0.36), (-3.9, -0.2, 0.39), (-2.4, -0.38, 0.43), (-0.2, 0.0, 0.44), (3.75, 0.0, 0.5)],
        [(-5.6, 1.8, 0.35), (-3.2, 1.55, 0.39), (-1.3, 1.12, 0.42), (0.9, 1.12, 0.43), (3.45, 1.28, 0.49)],
        [(-5.4, 0.85, 0.34), (-2.6, 0.7, 0.39), (-0.2, 0.38, 0.42), (1.4, 0.38, 0.43), (3.7, 0.0, 0.5)],
    ]
    for idx, points in enumerate(path_sets):
        add_line(f"governed flow path {idx + 1}", points, mats["line"], bevel_depth=0.012)
        pulse = add_sphere(f"active routing pulse {idx + 1}", points[0], 0.07, mats["forest"])
        animate_pulse(pulse, Vector(points[0]), Vector(points[-1]), 1 + idx * 28)

    # Quiet orientation labels for internal review; final Three.js hero should keep real text in HTML.
    add_label("ambiguity label", "AMBIGUITY", (-5.35, 2.72, 0.24), 0.16, mats["muted"])
    add_label("delivery label", "DELIVERY LAYER", (-0.15, 2.72, 0.24), 0.16, mats["forest"])
    add_label("proof label", "OPERATING PROOF", (4.28, 2.72, 0.24), 0.16, mats["white"])

    # Camera and lighting: calm executive control-surface view, not a sci-fi orbit.
    bpy.ops.object.light_add(type="AREA", location=(-2.2, -3.8, 5.5))
    key = bpy.context.object
    key.name = "large soft overhead light"
    key.data.energy = 640
    key.data.size = 7.5

    bpy.ops.object.light_add(type="POINT", location=(4.8, 2.3, 1.7))
    accent = bpy.context.object
    accent.name = "small proof accent light"
    accent.data.energy = 55
    accent.data.color = (0.40, 0.86, 0.40)

    bpy.ops.object.camera_add(location=(0.15, -6.8, 4.1), rotation=(math.radians(60), 0, 0))
    camera = bpy.context.object
    camera.name = "hero wide camera"
    bpy.context.scene.camera = camera
    camera.data.lens = 29
    camera.data.dof.use_dof = True
    camera.data.dof.focus_distance = 6.2
    camera.data.dof.aperture_fstop = 8.0

    # Render settings.
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.taa_render_samples = 64
    scene.render.resolution_x = 1800
    scene.render.resolution_y = 1000
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "Filmic"
    scene.view_settings.look = "Medium High Contrast"
    scene.world = bpy.data.worlds.new("dark hero world")
    scene.world.color = COLORS["currant"][:3]


def save_outputs() -> None:
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    bpy.context.scene.render.filepath = str(PREVIEW_PATH)
    bpy.ops.render.render(write_still=True)
    bpy.ops.export_scene.gltf(
        filepath=str(GLB_PATH),
        export_format="GLB",
        export_yup=True,
        export_apply=True,
        export_animations=True,
        export_lights=False,
        export_cameras=False,
    )


if __name__ == "__main__":
    build_scene()
    save_outputs()
