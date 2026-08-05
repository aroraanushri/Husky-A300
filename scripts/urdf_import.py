from isaacsim import SimulationApp

app = SimulationApp({"headless": False})

from isaacsim.asset.importer.urdf import (
    URDFImporter,
    URDFImporterConfig,
)

cfg = URDFImporterConfig()

cfg.urdf_path = "/home/anushri/husky_assignment/assets/husky_a300.urdf"

cfg.usd_path = "/home/anushri/husky_assignment/usd"

cfg.merge_fixed_joints = True
cfg.merge_mesh = False
cfg.debug_mode = True

cfg.collision_from_visuals = False
cfg.allow_self_collision = False

cfg.fix_base = False

importer = URDFImporter(cfg)

usd_path = importer.import_urdf()

print("USD generated:")
print(usd_path)

while app.is_running():
    app.update()

app.close()