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

fbrp.main()
