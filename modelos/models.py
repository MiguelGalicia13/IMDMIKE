from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.database import Base

class Movie(Base):
    #Id name description Length Director review
    __tablename__= 'Movies'
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(255))
    description = Column(String(500))
    length = Column(Integer)
    director = Column(String(255))
    review = relationship("Review", back_populates="movie")

class Review(Base):
    #Id movie_id rating comment movie
    __tablename__= 'Reviews'
    id = Column(Integer, primary_key=True, index = True)
    movie_id = Column(Integer, ForeignKey('Movies.id'))
    rating = Column(Float)
    comment = Column(String(500))
    movie = relationship("Movie", back_populates="review")

