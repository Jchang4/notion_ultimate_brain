# Notion API for Ultimate Brain
This is a Python API to interact with [Thomas Frank's Ultimate Brain Notion Template](). The functionality currently revolves around Projects and Tasks. But more features for Areas, Resources, Goals, etc. are on the way. 

On top of the Ultimate Brain specific features, you have full access to the [`notion_client`]() API to access all of your Notion databases and pages. 

# Demo
**TODO: add video**

# Installation
```bash
git clone <repo> && cd <repo> && pip install notion_client
```

Next you'll need to setup your `.env` file to include:
* `NOTION_TOKEN` = API token from Notion. Note you'll have to give your Workflow access to each Database/Page explicitely through the Notion UI
* `UB_ROOT_BLOCK_ID` = the ID of the Ultimate Brain root directory in Notion
* `UB_NOTES_DATABASE` = ID of the Notes database
* `UB_MILESTONES_DATABASE` = ID of the Milestones database
* `UB_PROJECTS_DATABASE` = ID of the Projects database
* `UB_TASKS_DATABASE` = ID of the Tasks database
* `UB_GOALS_DATABASE` = ID of the Goals database
* `UB_AREAS_AND_RESOURCES_DATABASE` = ID of the Areas & Resources database

In the future I can fetch these and write them to the `.env` file but for now you'll have to do it manually.

# Examples

## Get All Ultimate Brain Databases
```python
from notion_ultimate_brain.notion_ultimate_brain.all import UltimateBrainNotionClient

notion = UltimateBrainNotionClient()
print(notion.get_ub_databases())
```

## Get All Projects
```python
from notion_ultimate_brain.notion_ultimate_brain.all import UltimateBrainNotionClient

notion = UltimateBrainNotionClient()
print(notion.projects.get_pages())
```

## Get Tasks for Projects
```python
from notion_ultimate_brain.notion_ultimate_brain.all import UltimateBrainNotionClient

notion = UltimateBrainNotionClient()
project = next(iter(notion.projects.get_pages()))

print(project.all_tasks)
print(project.yesterday_tasks)
print(project.today_tasks)
print(project.tomorrow_tasks)
print(project.get_completed_tasks())
```

## Get Tasks for Tasks
```python
from notion_ultimate_brain.notion_ultimate_brain.all import UltimateBrainNotionClient

notion = UltimateBrainNotionClient()
task = next(iter(notion.tasks.get_pages()))

print(task.all_tasks)
print(task.yesterday_tasks)
print(task.today_tasks)
print(task.tomorrow_tasks)
print(task.get_completed_tasks())
```

# Future Work

* Add support for other databases - e.g. Areas, Resources, Goals, Milestone
* Add caching layer
* Automatically fetch `.env` IDs