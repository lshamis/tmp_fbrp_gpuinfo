import fbrp

fbrp.process(
    name="gpuinfo",
    runtime=fbrp.Conda(
        channels=[
            "conda-forge",
        ],
        dependencies=[
            "python>=3.7",
            "libgcc",
            {"pip": ["alephzero", "xmltodict"]},
        ],
        run_command=["python3", "gpuinfo.py"],
    ),
)

fbrp.process(
    name="api",
    runtime=fbrp.Docker(image="ghcr.io/alephzero/api:latest"),
)

fbrp.process(
    name="logger",
    runtime=fbrp.Docker(
        image="ghcr.io/alephzero/log:latest",
        mount=["/tmp/logs:/tmp/logs"],
    ),
    cfg={
        "savepath": "/tmp/logs",
        "default_max_logfile_duration": "2m",
        "rules": [
            {
                "protocol": "pubsub",
                "topic": "gpuinfo",
                "policies": [{"type": "save_all"}],
            }
        ],
    },
)

fbrp.main()
