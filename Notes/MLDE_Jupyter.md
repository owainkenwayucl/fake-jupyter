# Notes on supporting MLDE/determined.ai

## User experience:

Users install the determined.ai CLI and write a `config.yaml` file with settings for the notebook container.  Then at a shell they do:

```shell
$ det notebook ...
```

This creates a container and sets up forwarding automatically so that the notebook can be accessed through the MLDE web GUI + auth.

We want to be able to do this with other "notebooks", initially Pluto.jl but also things like PolyNote/RStudio.

It would be *super* nice if we could also make this work from the "Launch NotebooK" buttons in the Web GUI.

When MLDE starts a "notebook" container, it runs [the entrypoint shell script](https://github.com/determined-ai/determined/blob/main/master/static/srv/notebook-entrypoint.sh).  This has a `jupyter lab ...` command hard coded into it and the easiest way of supporting this seamlessly with other providers is to override the `jupyter` command within the container with one that starts our chosen provider with the right options converted.
