from .base import Base
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey

# Define the view query as a string
projects_view_query = '''
CREATE OR REPLACE VIEW projects_view AS (
    SELECT 
        projects.project_id,
        projects.project_name,
        projects.UCRA_id,
        projects.model_id,
        project_status.status_name AS project_status,
        campaigns.campaign_name,
        project_offer_codes.offer_code,
        channels.channel_level_1,
        channels.channel_level_2,
        channels.channel_level_3,
        project_tasks.task_name,
        project_tasks.task_description,
        task_categories.task_category_name AS task_category,
        task_flow.task_flow_name AS task_flow,
        task_status.task_status_name AS task_status,
        project_tasks.task_due_date,
        project_tasks.task_completed_date
    FROM projects
    LEFT JOIN project_status ON projects.status_id = project_status.status_id
    LEFT JOIN project_offer_codes ON projects.project_id = project_offer_codes.project_id
    LEFT JOIN campaigns ON project_offer_codes.campaign_id = campaigns.campaign_id
    LEFT JOIN project-channels ON projects.project_id = project_channels.project_id
    LEFT JOIN channels ON project_channels.channel_id = channels.channel_id
    LEFT JOIN project_tasks ON 
        (projects.project_id = project_tasks.project_id
        AND project_tasks.offer_code = project_offer_codes.offer_code
        AND project_tasks.channel_id = project_channels.channel_id)
    LEFT JOIN task_categories ON project_tasks.task_category_id = task_categories.task_category_id
    LEFT JOIN task_flow ON project_tasks.task_flow_id = task_flow.task_flow_id
    LEFT JOIN task_status ON project_tasks.task_status_id = task_status.task_status_id
);
'''

# Define the SQLAlchemy table object that references the view
projects_view_table = Table(
    'projects_view',
    Base.metadata,
    Column('project_id', Integer, primary_key=True),
    Column('project_name', String(50), nullable=False),
    Column('UCRA_id', Integer),
    Column('model_id', Integer),
    Column('project_status', Integer),
    Column('campaign_name', String(50)),
    Column('offer_code', String(50)),
    Column('channel_level_1', String(50)),
    Column('channel_level_2', String(50)),
    Column('channel_level_3', String(50)),
    Column('task_name', String(50)),
    Column('task_description', String(100)),
    Column('task_category', String(50)),
    Column('task_flow', String(50)),
    Column('task_status', String(50)),
    Column('task_due_date', Date, nullable=False),
    Column('task_completed_date', Date, nullable=False),
    extend_existing=True
)

# Define the ProjectsView model
class ProjectsView(Base):
    __table__ = projects_view_table
