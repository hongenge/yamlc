from yamlio.yamlio import Yamlio

Yamlio.set_config_file_path("config.yaml")

print(Yamlio.get("app.name"))
print(Yamlio.get("api.base_url"))
