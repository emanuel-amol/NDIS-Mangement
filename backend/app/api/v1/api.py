# backend/app/api/v1/api.py - UPDATED VERSION WITH DOCUMENT VERSIONS
from fastapi import APIRouter
from app.api.v1.endpoints.referral import router as referral_router
from app.api.v1.endpoints.participant import router as participant_router
from app.api.v1.endpoints.care_workflow import router as care_workflow_router
from app.api.v1.endpoints.document import router as document_router
from app.api.v1.endpoints.document_generation import router as document_generation_router
from app.api.v1.endpoints.document_workflow import router as document_workflow_router
from app.api.v1.endpoints.document_versions import router as document_versions_router

api_router = APIRouter()

# Include all routers with proper prefixes and tags
api_router.include_router(referral_router, prefix="/participants", tags=["referrals"])
api_router.include_router(participant_router, prefix="/participants", tags=["participants"])
api_router.include_router(care_workflow_router, prefix="/care", tags=["care-workflow"])
api_router.include_router(document_router, prefix="", tags=["documents"])
api_router.include_router(document_generation_router, prefix="", tags=["document-generation"])
api_router.include_router(document_workflow_router, prefix="/document-workflow", tags=["document-workflow"])
api_router.include_router(document_versions_router, prefix="", tags=["document-versions"])