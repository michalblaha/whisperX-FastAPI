from pydantic import BaseModel, validator
from typing import Optional, List, Union

class NoValidationBaseModel(BaseModel):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return v  # simply return the value without validation


class Response(NoValidationBaseModel):
    identifier: str
    message: str


class Metadata(NoValidationBaseModel):
    task_type: str
    file_name: Optional[str]
    duration: Optional[float]


class Task(NoValidationBaseModel):
    identifier: str
    status: str
    task_type: str


class ResultTasks(NoValidationBaseModel):
    tasks: List[Task]


class TranscriptionSegment(NoValidationBaseModel):
    start: float
    end: float
    text: str


class Segment(NoValidationBaseModel):
    start: float
    end: float
    text: Optional[str]
    speaker: Optional[str]


class Word(NoValidationBaseModel):
    word: str
    start: float
    end: float
    score: float


class AlingmentSegment(NoValidationBaseModel):
    start: float
    end: float
    text: str
    words: List[Word]


class AlignedTranscription(NoValidationBaseModel):
    segments: List[AlingmentSegment]
    word_segments: List[Word]


class DiarizationSegment(NoValidationBaseModel):
    label: str
    speaker: str
    start: float
    end: float


class DiaredTrancript(NoValidationBaseModel):
    segments: List[Segment]


class Transcript(NoValidationBaseModel):
    segments: List[TranscriptionSegment]
    language: Optional[str]


class TranscriptInput(NoValidationBaseModel):
    transcript: Transcript


class Result(NoValidationBaseModel):
    status: str
    result: Optional[
        Union[
            List[DiarizationSegment],
            Transcript,
            DiaredTrancript,
            AlignedTranscription,
        ]
    ]
    metadata: Metadata
    error: Optional[str]
