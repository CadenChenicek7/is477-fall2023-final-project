rule prepare:
    output:
        "data/iris/iris.data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/iris/iris.data"
    output:
        "profiling/iris_report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    input:
        "data/iris/iris.data"
    output:
        "results/iris_vis.png"
    shell:
        "python scripts/analysis.py"
