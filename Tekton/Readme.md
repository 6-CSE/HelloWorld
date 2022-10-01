# Tekton (Cloud native CI/CD Tool)

### Installation

* Install tkn, the [Tekton CLI](https://tekton.dev/docs/cli/)



### How to run a pipeline

1. Create Tasks

    ```bash
    $ kubectl apply -f hello-world.yaml
    $ kubectl apply -f goodbye-world.yaml
    ```
    
2. Create a pipeline run

    ```bash
    $ kubectl apply --filename tkn-pipeline.yaml
    ```

3. Create & Run a PipelineRun
    
    ```bash
    $ kubectl apply --filename tkn-pipeline-run.yaml
    ``` 



### Logs of a pipeline

```bash
$ tkn pipelinerun logs tkn-pipeline-run -f -n default
```