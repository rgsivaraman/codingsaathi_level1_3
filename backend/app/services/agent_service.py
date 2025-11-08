"""Agent service for business logic."""
from sqlalchemy.orm import Session

from app.models.agent import Agent


class AgentService:
    """Service for managing agents."""
    
    @staticmethod
    def get_agent(db: Session, agent_id: int) -> Agent | None:
        """Get an agent by ID."""
        return db.query(Agent).filter(Agent.id == agent_id).first()
    
    @staticmethod
    def get_agents(db: Session, skip: int = 0, limit: int = 100) -> list[Agent]:
        """Get list of agents."""
        return db.query(Agent).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_agent(db: Session, name: str, description: str = None, author: str = None) -> Agent:
        """Create a new agent."""
        agent = Agent(
            name=name,
            description=description,
            author=author,
        )
        db.add(agent)
        db.commit()
        db.refresh(agent)
        return agent
    
    @staticmethod
    def update_agent(db: Session, agent_id: int, **kwargs) -> Agent | None:
        """Update an agent."""
        agent = AgentService.get_agent(db, agent_id)
        if agent:
            for key, value in kwargs.items():
                if hasattr(agent, key):
                    setattr(agent, key, value)
            db.commit()
            db.refresh(agent)
        return agent
    
    @staticmethod
    def delete_agent(db: Session, agent_id: int) -> bool:
        """Delete an agent."""
        agent = AgentService.get_agent(db, agent_id)
        if agent:
            db.delete(agent)
            db.commit()
            return True
        return False
