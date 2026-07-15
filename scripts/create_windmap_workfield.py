from __future__ import annotations

import math
import random
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "3d"
BLEND_PATH = OUT_DIR / "windmap-workfield.blend"
GLB_PATH = OUT_DIR / "windmap-workfield.glb"
PREVIEW_PATH = OUT_DIR / "windmap-workfield-preview.png"


COLORS = {
    "currant": (0.009, 0.012, 0.055, 1.0),
    "currant_lift": (0.035, 0.035, 0.14, 1.0),
    "teal": (0.14, 0.42, 0.43, 1.0),
    "deep_teal": (0.04, 0.18, 0.23, 1.0),
    "forest": (0.37, 0.74, 0.36, 1.0),
    "cream": (0.78, 0.80, 0.65, 1.0),
    "tangerine": (0.98, 0.65, 0.09, 1.0),
    "plum": (0.31, 0.04, 0.27, 1.0),
    "white": (0.92, 0.94, 0.97, 1.0),
    "muted": (0.45, 0.54, 0.62, 1.0),
}


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 180


def mat_principled(
    name: str,
    color: tuple[float, float, float, float],
    *,
    roughness: float = 0.65,
    alpha: float = 1.0,
    emission_strength: float = 0.0,
) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        rgba = (color[0], color[1], color[2], alpha)
        bsdf.inputs["Base Color"].default_value = rgba
        bsdf.inputs["Alpha"].default_value = alpha
        bsdf.inputs["Roughness"].default_value = roughness
        if emission_strength:
            bsdf.inputs["Emission Color"].default_value = color
            bsdf.inputs["Emission Strength"].default_value = emission_strength
    mat.blend_method = "BLEND"
    mat.use_screen_refraction = True
    return mat


def mat_textured(name: str, base: tuple[float, float, float, float], accent: tuple[float, float, float, float]) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 18
    noise.inputs["Detail"].default_value = 12
    noise.inputs["Roughness"].default_value = 0.62
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.24
    ramp.color_ramp.elements[0].color = base
    ramp.color_ramp.elements[1].position = 1.0
    ramp.color_ramp.elements[1].color = accent
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.08
    bump.inputs["Distance"].default_value = 0.05
    if bsdf:
        bsdf.inputs["Roughness"].default_value = 0.82
        links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
        links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
        links.new(noise.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def add_box(name: str, loc: tuple[float, float, float], scale: tuple[float, float, float], mat: bpy.types.Material, bevel: float = 0.025) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    if bevel:
        mod = obj.modifiers.new("softened edges", "BEVEL")
        mod.width = bevel
        mod.segments = 2
        obj.modifiers.new("weighted normals", "WEIGHTED_NORMAL")
    return obj


def add_curve(name: str, points: list[tuple[float, float, float]], mat: bpy.types.Material, bevel: float) -> bpy.types.Object:
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 18
    curve.bevel_depth = bevel
    curve.bevel_resolution = 2
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for p, coords in zip(spline.points, points):
        p.co = (coords[0], coords[1], coords[2], 1)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    return obj


def add_ribbon(name: str, y_offset: float, z_offset: float, width: float, mat: bpy.types.Material, phase: float, amp: float) -> bpy.types.Object:
    verts: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int, int]] = []
    segments = 72
    for i in range(segments + 1):
        t = i / segments
        x = -7.4 + t * 14.8
        y = y_offset + math.sin(t * math.tau * 1.55 + phase) * amp + math.sin(t * math.tau * 3.2 + phase) * 0.14
        z = z_offset + math.sin(t * math.tau * 1.1 + phase) * 0.18
        dx = 0.1
        y2 = y_offset + math.sin((t + dx) * math.tau * 1.55 + phase) * amp
        tangent = Vector((1, y2 - y, 0)).normalized()
        normal = Vector((-tangent.y, tangent.x, 0)).normalized()
        verts.append((x + normal.x * width, y + normal.y * width, z))
        verts.append((x - normal.x * width, y - normal.y * width, z))
        if i < segments:
            a = i * 2
            faces.append((a, a + 1, a + 3, a + 2))
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    mod = obj.modifiers.new("ribbon weighted normals", "WEIGHTED_NORMAL")
    return obj


def animate_pulse(obj: bpy.types.Object, points: list[tuple[float, float, float]], offset: int) -> None:
    obj.location = points[0]
    obj.keyframe_insert(data_path="location", frame=1 + offset)
    obj.location = points[-1]
    obj.keyframe_insert(data_path="location", frame=120 + offset)
    obj.location = points[0]
    obj.keyframe_insert(data_path="location", frame=180 + offset)


def add_sphere(name: str, loc: tuple[float, float, float], radius: float, mat: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=radius, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def build_scene() -> None:
    clear_scene()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    random.seed(42)

    mats = {
        "field": mat_principled("deep currant hero field", COLORS["currant"], roughness=0.9),
        "teal_texture": mat_textured("service-art teal texture", COLORS["deep_teal"], COLORS["cream"]),
        "green_texture": mat_textured("service-art green texture", COLORS["teal"], COLORS["forest"]),
        "plum_texture": mat_textured("service-art currant plum texture", COLORS["plum"], COLORS["cream"]),
        "wind": mat_principled("soft windmap streamline", COLORS["forest"], alpha=0.58, emission_strength=1.1),
        "wind_dim": mat_principled("dim windmap streamline", COLORS["teal"], alpha=0.34, emission_strength=0.45),
        "grid": mat_principled("service-art grid marks", COLORS["muted"], alpha=0.42, emission_strength=0.1),
        "proof": mat_principled("operating proof marker", COLORS["tangerine"], alpha=0.9, emission_strength=0.65),
        "white": mat_principled("quiet white", COLORS["white"], alpha=0.92),
    }

    add_box("deep currant background", (0, 0, -0.28), (18.5, 9.4, 0.08), mats["field"], bevel=0)

    # Service-image-style textured layers: painterly ribbons, not literal UI.
    add_ribbon("wide teal workstream surface", -0.65, 0.05, 0.34, mats["teal_texture"], phase=0.1, amp=0.55)
    add_ribbon("cream-green decision surface", 0.28, 0.18, 0.26, mats["green_texture"], phase=1.25, amp=0.42)
    add_ribbon("currant-plum embedded surface", 1.02, 0.0, 0.23, mats["plum_texture"], phase=2.1, amp=0.38)

    # Windmap streamlines that start loose and become more directional.
    for i in range(34):
        y_base = -2.65 + i * 0.16
        phase = random.uniform(0, math.tau)
        points = []
        for step in range(42):
            t = step / 41
            x = -7.6 + t * 15.2
            turbulence = (1 - t) * 0.55
            y = y_base + math.sin(t * math.tau * 1.9 + phase) * (0.18 + turbulence)
            z = 0.35 + math.sin(t * math.tau * 1.2 + phase) * 0.16 + t * 0.1
            points.append((x, y, z))
        add_curve(f"windmap streamline {i + 1:02d}", points, mats["wind" if i % 3 == 0 else "wind_dim"], bevel=0.006 if i % 3 else 0.011)

    # Sparse decision gates and proof markers embedded in the flow.
    for idx, x in enumerate([-2.25, -0.45, 1.35, 3.15]):
        add_box(f"decision gate {idx + 1}", (x, -0.05, 0.44), (0.055, 3.25 - idx * 0.24, 0.18), mats["grid"], bevel=0.01)
        add_sphere(f"governance node {idx + 1}", (x, 1.45 - idx * 0.24, 0.62), 0.08, mats["proof" if idx == 2 else "wind"])

    for idx, (x, y) in enumerate([(4.45, 0.95), (5.15, 0.05), (4.25, -0.95)]):
        marker = add_box(f"proof output marker {idx + 1}", (x, y, 0.5), (0.72, 0.18, 0.08), mats["proof"], bevel=0.025)
        marker.rotation_euler[2] = -0.08

    # Small animated pulses for Three.js export.
    pulse_paths = [
        [(-6.5, -1.4, 0.58), (-2.3, -0.8, 0.7), (1.3, -0.35, 0.72), (4.6, -0.1, 0.76)],
        [(-6.2, 0.75, 0.62), (-1.8, 0.5, 0.73), (1.7, 0.36, 0.76), (4.5, 0.86, 0.78)],
        [(-5.9, -0.15, 0.6), (-0.4, 0.0, 0.72), (3.6, -0.85, 0.77)],
    ]
    for idx, path in enumerate(pulse_paths):
        add_curve(f"active routed path {idx + 1}", path, mats["wind"], bevel=0.015)
        pulse = add_sphere(f"animated routing pulse {idx + 1}", path[0], 0.065, mats["proof" if idx == 1 else "wind"])
        animate_pulse(pulse, path, idx * 34)

    # Faint service-art grid marks.
    for idx, x in enumerate([-5.2, -4.7, 2.8, 3.25, 3.7]):
        add_curve(f"vertical texture grid {idx + 1}", [(x, -2.2, 0.31), (x, -0.4 + idx * 0.15, 0.34)], mats["grid"], bevel=0.004)
    for idx, y in enumerate([-1.95, -1.55, 1.9, 2.22]):
        add_curve(f"horizontal texture grid {idx + 1}", [(-5.5, y, 0.32), (-3.5 + idx * 0.35, y, 0.34)], mats["grid"], bevel=0.004)

    # Camera leaves negative space on left/center for HTML hero copy.
    bpy.ops.object.light_add(type="AREA", location=(-2.6, -4.2, 5.4))
    key = bpy.context.object
    key.name = "large soft hero light"
    key.data.energy = 520
    key.data.size = 7.2

    bpy.ops.object.light_add(type="POINT", location=(4.6, 2.0, 1.8))
    accent = bpy.context.object
    accent.name = "proof marker accent light"
    accent.data.energy = 85
    accent.data.color = (0.7, 0.95, 0.45)

    bpy.ops.object.camera_add(location=(-0.45, -6.55, 3.55), rotation=(math.radians(58), 0, math.radians(-1.5)))
    camera = bpy.context.object
    camera.name = "windmap hero camera"
    bpy.context.scene.camera = camera
    camera.data.lens = 26

    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.taa_render_samples = 64
    scene.render.resolution_x = 1800
    scene.render.resolution_y = 1000
    scene.view_settings.view_transform = "Filmic"
    scene.view_settings.look = "Medium High Contrast"
    scene.world = bpy.data.worlds.new("currant world")
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
