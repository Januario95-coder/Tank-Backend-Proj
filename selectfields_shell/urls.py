from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    impressedCoatingAppliedToSheelPlatesView,
    ExternalCoatingAppliedToShellPlatesView,
    StorageConditionsView,
    HeatedCoilsInTankView,
    ProductCorrosivityView,
    VaporCorrosivityView,
    TankShellHasBeenInsulatedView,
    TimeToRepairView,
    CostOfRepairView,
    ProbableMagnitudeOfProductLossView,
    LikelihoodOfInjuryToPersonnelView,
    ProductFlammabilityAsPerMCSPView,
    ProductToxicityView,
    LocationOfTankFarmView
)


router = DefaultRouter()
router.register('impress-cathodic', impressedCoatingAppliedToSheelPlatesView, basename='impressedCoatingAppliedToSheelPlates')
router.register('sacrificial-cathodic', ExternalCoatingAppliedToShellPlatesView, basename='ExternalCoatingAppliedToShellPlates')
router.register('storage-conditions', StorageConditionsView, basename='StorageConditions')
router.register('heating-coils', HeatedCoilsInTankView, basename='HeatedCoilsInTank')
router.register('product-corrosivity', ProductCorrosivityView, basename='ProductCorrosivity')
router.register('vapous-corrosivity', VaporCorrosivityView, basename='VaporCorrosivity')
router.register('tank-shell-insulateds', TankShellHasBeenInsulatedView, basename='TankShellHasBeenInsulated')
router.register('time-to-repair', TimeToRepairView, basename='TimeToRepair')
router.register('cost-of-repair', CostOfRepairView, basename='CostOfRepair')
router.register('problable-magnitude', ProbableMagnitudeOfProductLossView, basename='ProbableMagnitudeOfProductLoss')
router.register('likelihood-of-injury', LikelihoodOfInjuryToPersonnelView, basename='LikelihoodOfInjuryToPersonnel')
router.register('product-flamability', ProductFlammabilityAsPerMCSPView, basename='ProductFlammabilityAsPerMCSP')
router.register('product-toxicity', ProductToxicityView, basename='ProductToxicity')
router.register('location-of-tank', LocationOfTankFarmView, basename='LocationOfTankFarm')


urlpatterns = [
    path('', include(router.urls))
]