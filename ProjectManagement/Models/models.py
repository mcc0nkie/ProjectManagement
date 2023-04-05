from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, select, text, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class RecordsUCRA(Base):
    __tablename__ = 'UCRA'
    __table_args__ = {'schema': 'records'}
    UCRA = Column(String(20), primary_key=True)
    UCRA_description = Column(String(100), nullable=False)


class RecordsModels(Base):
    __tablename__ = 'models'
    __table_args__ = {'schema': 'records'}
    model_id = Column(String(20), primary_key=True)
    model_name = Column(String(50), nullable=False)
    model_description = Column(String(100), nullable=False)


class RecordsChannels(Base):
    __tablename__ = 'channels'
    __table_args__ = {'schema': 'records'}
    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    channel_level_1 = Column(String(50), nullable=False)
    channel_level_2 = Column(String(50), nullable=False)
    channel_level_3 = Column(String(50), nullable=False)
    channel_description = Column(String(100), nullable=False)


class RecordsLOB(Base):
    __tablename__ = 'LOB'
    __table_args__ = {'schema': 'records'}
    LOB_id = Column(Integer, primary_key=True, autoincrement=True)
    LOB_name = Column(String(50), nullable=False)
    LOB_description = Column(String(100), nullable=False)


class RecordsCampaigns(Base):
    __tablename__ = 'campaigns'
    __table_args__ = {'schema': 'records'}
    campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_name = Column(String(50), nullable=False)
    campaign_description = Column(String(100), nullable=False)
    LOB_id = Column(Integer, ForeignKey('records.LOB.LOB_id'))


class RecordsOfferCodes(Base):
    __tablename__ = 'offer_codes'
    __table_args__ = {'schema': 'records'}
    offer_code = Column(String(50), primary_key=True)
    offer_code_name = Column(String(50), nullable=False)
    offer_code_description = Column(String(100), nullable=False)    


class RecordsTaskStatus(Base):
    __tablename__ = 'task_status'
    __table_args__ = {'schema': 'records'}
    task_status_id = Column(Integer, primary_key=True, autoincrement=True)
    task_status_name = Column(String(50), nullable=False)
    task_status_description = Column(String(100), nullable=False)


class RecordsTaskFlow(Base):
    __tablename__ = 'task_flow'
    __table_args__ = {'schema': 'records'}
    task_flow_id = Column(Integer, primary_key=True, autoincrement=True)
    task_flow_name = Column(String(50), nullable=False)
    task_flow_description = Column(String(100), nullable=False)


class RecordsTaskCategories(Base):
    __tablename__ = 'task_categories'
    __table_args__ = {'schema': 'records'}
    task_category_id = Column(Integer, primary_key=True, autoincrement=True)
    task_category_name = Column(String(50), nullable=False)
    task_category_description = Column(String(100), nullable=False)


class RecordsTasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'records'}
    task_id = Column(Integer, primary_key=True)
    task_name = Column(String(100), nullable=False)
    task_description = Column(String(100), nullable=False)
    task_category_id = Column(Integer, ForeignKey('records.task_categories.task_category_id'))


class TrackingProjects(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(50), nullable=False)
    project_description = Column(String(100), nullable=False)


class TrackingProjectsUCRA(Base):
    __tablename__ = 'projects_ucra'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    UCRA = Column(String(20), ForeignKey('tracking.UCRA.UCRA'), primary_key=True)


class TrackingProjectsModels(Base):
    __tablename__ = 'projects_models'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    model_id = Column(String(20), ForeignKey('tracking.models.model_id'), primary_key=True)


class TrackingProjectsChannels(Base):
    __tablename__ = 'projects_channels'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    channel_id = Column(Integer, ForeignKey('tracking.channels.channel_id'), primary_key=True)


class TrackingProjectsCampaigns(Base):
    __tablename__ = 'projects_campaigns'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    campaign_id = Column(Integer, ForeignKey('tracking.campaigns.campaign_id'), primary_key=True)


class TrackingProjectsOfferCodes(Base):
    __tablename__ = 'projects_offer_codes'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    offer_code = Column(String(50), ForeignKey('tracking.offer_codes.offer_code'), primary_key=True)


class TrackingProjectsTasks(Base):
    __tablename__ = 'projects_tasks'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tracking.tasks.task_id'), primary_key=True)
    task_workflow_id = Column(Integer, ForeignKey('tracking.task_flow.task_flow_id'), primary_key=True)
    task_status_id = Column(Integer, ForeignKey('tracking.task_status.task_status_id'), primary_key=True)


class TrackingProjectsTasksNotes(Base):
    __tablename__ = 'projects_tasks_notes'
    __table_args__ = {'schema': 'tracking'}
    project_id = Column(Integer, ForeignKey('tracking.projects.project_id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tracking.tasks.task_id'), primary_key=True)
    note_id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)


def CreateMasterView():

    '''
    Create master view; join all the project tables together and grab value names from the records tables
    '''
    select_statement = select(
            TrackingProjects.project_id,
            TrackingProjects.project_name,
            TrackingProjects.project_description,
            TrackingProjectsLOBs.LOB_name,
            RecordsUCRA.UCRA,
            RecordsModels.model_name,
            RecordsChannels.channel_level_1,
            RecordsChannels.channel_level_2,
            RecordsChannels.channel_level_3,
            RecordsCampaigns.campaign_name,
            RecordsOffercodes.offer_code,
            RecordsTasks.task_name,
            RecordsTaskCategories.task_category_name,
            RecordsTaskFlow.task_flow_name,
            RecordsTaskStatus.task_status_name
        ).select_from(
            TrackingProjects.__table__.join(
                TrackingProjectsLOBs.__table__,
                TrackingProjectsLOBs.project_id == TrackingProjects.project_id
            ).join(
                TrackingProjectsUCRA.__table__,
                TrackingProjectsUCRA.project_id == TrackingProjects.project_id
            ).join(
                TrackingProjectsModels.__table__,
                TrackingProjectsModels.project_id == TrackingProjects.project_id
            ).join(
                TrackingProjectsChannels.__table__,
                TrackingProjectsChannels.project_id == TrackingProjects.project_id
            ).join(
                TrackingProjectsCampaigns.__table__,
                TrackingProjectsCampaigns.project_id == TrackingProjects.project_id
            ).join(
                TrackingProjectsOfferCodes.__table__,
                TrackingProjectsOfferCodes.project_id == TrackingProjects.project_id
            ).join(
                TrackingProjectsTasks.__table__,
                TrackingProjectsTasks.project_id == TrackingProjects.project_id
            ).join(
                RecordsUCRA.__table__,
                RecordsUCRA.UCRA == TrackingProjectsUCRA.UCRA
            ).join(
                RecordsModels.__table__,
                RecordsModels.model_id == TrackingProjectsModels.model_id
            ).join(
                RecordsChannels.__table__,
                RecordsChannels.channel_id == TrackingProjectsChannels.channel_id
            ).join(
                RecordsCampaigns.__table__,
                RecordsCampaigns.campaign_id == TrackingProjectsCampaigns.campaign_id
            ).join(
                RecordsOffercodes.__table__,
                RecordsOffercodes.offer_code == TrackingProjectsOfferCodes.offer_code
            ).join(
                RecordsTasks.__table__,
                RecordsTasks.task_id == TrackingProjectsTasks.task_id
            ).join(
                RecordsTaskCategories.__table__,
                RecordsTaskCategories.task_category_id == RecordsTasks.task_category_id
            ).join(
                RecordsTaskFlow.__table__,
                RecordsTaskFlow.task_flow_id == TrackingProjectsTasks.task_workflow_id
            ).join(
                RecordsTaskStatus.__table__,
                RecordsTaskStatus.task_status_id == TrackingProjectsTasks.task_status_id
            )
        )

    master_view = select_statement.alias('master_view')
    return master_view


class Logs(Base):
    __tablename__ = 'logs'
    __table_args__ = {'schema': 'logs'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    schema_name = Column(String(50), nullable=False)
    table_name = Column(String(50), nullable=False)
    record_id = Column(Integer, nullable=False)
    action = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)


if __name__ == '__main__':
    engine = create_engine('sqlite:///ProjectManagement.db')
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    master_view = CreateMasterView()
    session.execute(CreateView(master_view))

    session.commit()
    session.close()
