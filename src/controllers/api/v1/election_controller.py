from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/{vote}")
def election(vote : str):
    return{
        "You are Voting":vote
    }

@router.get("/{vote}/{nid}")
def election_with_nid(vote : str, nid : int):    
    return{
        "You are Voting " : vote,
        "Your NID number " : nid 
    }

@router.get("/{vote}")
def election_vote(vote : str, nid: Optional[int]=None):    
    return{
        "You are Voting" : vote,
        "Your NID number " : nid 
    }