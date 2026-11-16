# Workspace: second computer

!!! info "Full version only"
    OurPlanCore Lite has no Workspace: no `Settings > Workspace` section and no background sync. In Lite, a job is passed on as a copy of the saved `.ourplan` file ([Jobs and saving](job-creation-storage.md#file)). How the versions differ: [Lite vs full version](ourplancore-lite.md).

Here: the shared workspace of the full version: a private server, a second computer, shared jobs, presets and assistant conversations. You need it when working from a laptop. Importing one job into another is described in [Jobs and saving](job-creation-storage.md#import-project), the pipeline console `OurPlanCoreCli` [on the same page](job-creation-storage.md#cli), the module list in [Settings, Modules](ourplancore-settings.md#modules), the Job Tracker button in [Managers](ourplancore-managers.md#job-tracker).

## Workspace: a shared workspace {#workspace}

There is no screenshot of this section on purpose: it always shows the server address, the computer name and the names of current jobs.

**What it is.** A private server keeps shared rules and notes, agent skills, settings presets, selected saved jobs and archives of Claude and Codex conversations. The app works locally and syncs in the background; plan editing and the terminal do not wait for the server. The local folder by default is `Documents\OurPlanCore Workspace`; inside are `knowledge`, `skills`, `profile`, `projects`, `conversations` and `runtime` (a working projection for the assistants).

| Group in `Settings > Workspace` | Buttons and fields |
| --- | --- |
| This computer | `Use shared workspace`, device name, `Local workspace folder`, `Automatic synchronization` with an interval, categories (`Claude / Codex skills and supporting scripts`, `Shared conversation archives`), `Save`, `Sync now`, `Import this setup`, `Open local folder`, `Server status` |
| Workspace server | server address (stored on each device separately) |
| Connect another computer | `Create code for another computer` (a one-time code valid for 10 minutes), `Connect this computer` |
| Projects | `Share current saved project`, `Open selected`, `Review conflicts`, `Apply shared presets` |
| Conversations | `Continue selected`, `Setup on this computer`, `Import a Claude / Codex conversation` |

### How to connect a second computer { #second-pc }

What for: continue the same job from a laptop with the same rules and assistant conversations.
Needed: the app is installed on both computers; the server address is known.

1. On the main one, open **Settings > Workspace**, check **Use shared workspace**, connect the device and press **Import this setup** (the source folders do not change).
2. Press **Share current saved project** for the `.ourplan` you need: the package goes to the server, later saves sync by themselves.
3. On the second one, enter the server address and the code from **Create code for another computer** in **Settings > Workspace**, press **Connect this computer**. Rules and skills download; jobs and conversations on request.
4. Press **Projects > Open selected**: the shared job is open. The terminals on the new computer need Git Bash and a one-time login to the assistant CLI ([AI console](ourplancore-ai-console.md)).
5. Before switching computers, press ++ctrl+s++, then **Sync now** and wait for the Synced status.

Result: both computers see one job, presets and conversations; status `Synced` in Settings > Workspace.

### Conflicts and limits

- A conflict keeps both versions: `Review conflicts`, then `Keep this computer`, `Use server version` or `Open preserved files`.
- An open job is not replaced by the server version; a modified local file is not overwritten on download.
- Deletion does not spread between devices. Cached jobs and knowledge are available offline.
- Shared presets are applied only with the `Apply shared presets` button; job copies of settings still win; local presets are backed up first.
- A conversation over 256 MB is skipped with a warning, the rest sync (3.0).
- Keys, assistant logins and personal folders are not imported or synced.

## Modules { #modules }

The module list has moved: [Settings, Modules](ourplancore-settings.md#modules).

## OurPlanCoreCli { #cli }

The pipeline console has moved: [Jobs and saving, OurPlanCoreCli](job-creation-storage.md#cli).

## See also

- [AI console and terminal](ourplancore-ai-console.md): conversations from the `>_` panel and continuing them on a second computer
- [AI in the app](ourplancore-ai.md): Agent Bridge
- [Settings: all categories](ourplancore-settings.md)
- [Jobs and saving](job-creation-storage.md)
