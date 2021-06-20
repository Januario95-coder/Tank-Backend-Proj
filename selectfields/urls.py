from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ImpressCathodicProtectionView,
    SacrificialCathodicPropectionView,
    BottomPlatesInternalCoatingLiningView,
    BottomPlatesExternalCoatingView,
    StorageConditionsView,
    TypeOfBottomView,
    HeatingCoilsInTankView,
    ProductCorrosivityView,
    FoundationTypeView,
    HeightOfFoundationView,
    EffectivenessOfDrainageView,
    TimeToRepairView,
    CostOfRepairView,
    ProbableMagnitudeOfProductLossView,
    LikelihoodOfInjuryToPersonnelView,
    ProductFlammabilityAsPerMCSPView,
    ProductToxicityView,
    LocationOfTankFarmView,
    TankLocatedNearPublicFenceView,
    EnvironmetalHazardToSoilAndWaterView,
    VapourEmissionView,
    AccelerationFactorForPittingView,
    NDTMethodUsedForThicknessMeasurementsView,
    FrequencyOfInternalInspectionsView,
    NdtMethodQualificationOfNdtOperatorsView,
    EvidenceAvailableOfCompletingPdcaView,
    DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsView,
    AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamView,
    AretrainingrequirementsforrbiteammembersconsistentlyusedView,
    DoesTheItemEvaluationHaveSignificantPittingView,
    CanTheDegradationMechanismBeRegardedAsLinearView,
    IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationView,

    AreProceduresInPlaceToPreventWaterContactView,
    IsTheCorrosionRateDeterminedWithAtLeast2SourcesView,
    IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsView,
    WhichMethodIsUsedView
)


router = DefaultRouter()
router.register('impress-cathodic', ImpressCathodicProtectionView,
                basename='ImpressCathodicProtection')
router.register('sacrificial-cathodic', SacrificialCathodicPropectionView,
                basename='SacrificialCathodicPropection')
router.register('internal-coating', BottomPlatesInternalCoatingLiningView,
                basename='BottomPlatesInternalCoatingLining')
router.register('external-coating', BottomPlatesExternalCoatingView,
                basename='BottomPlatesExternalCoating')
router.register('storage-conditions', StorageConditionsView,
                basename='StorageConditions')
router.register('type-of-bottom', TypeOfBottomView, basename='TypeOfBottom')
router.register('heating-coils', HeatingCoilsInTankView,
                basename='HeatingCoilsInTank')
router.register('product-corrosivity', ProductCorrosivityView,
                basename='ProductCorrosivity')
router.register('foundation-type', FoundationTypeView,
                basename='FoundationType')
router.register('height-of-foundation', HeightOfFoundationView,
                basename='HeightOfFoundation')
router.register('effectivenessOf-drainage',
                EffectivenessOfDrainageView, basename='EffectivenessOfDrainage')
router.register('time-to-repair', TimeToRepairView, basename='TimeToRepair')
router.register('cost-of-repair', CostOfRepairView, basename='CostOfRepair')
router.register('drainage-magnitude', ProbableMagnitudeOfProductLossView,
                basename='ProbableMagnitudeOfProductLoss')
router.register('likelihood-of-injury', LikelihoodOfInjuryToPersonnelView,
                basename='LikelihoodOfInjuryToPersonnel')
router.register('product-flamability', ProductFlammabilityAsPerMCSPView,
                basename='ProductFlammabilityAsPerMCSP')
router.register('product-toxicity', ProductToxicityView,
                basename='ProductToxicity')
router.register('location-of-tank', LocationOfTankFarmView,
                basename='LocationOfTankFarm')
router.register('tank-located-near-public-fence', TankLocatedNearPublicFenceView,
                basename='TankLocatedNearPublicFence')
router.register('environmental-hazard', EnvironmetalHazardToSoilAndWaterView,
                basename='EnvironmetalHazardToSoilAndWater')
router.register('vapour-emission', VapourEmissionView,
                basename='VapourEmission')
router.register('accelaration-factor', AccelerationFactorForPittingView,
                basename='AccelerationFactorForPitting')
router.register('ndt-method-used', NDTMethodUsedForThicknessMeasurementsView,
                basename='NDTMethodUsedForThicknessMeasurements')
router.register('freq-of-internal-insp', FrequencyOfInternalInspectionsView,
                basename='FrequencyOfInternalInspections')
router.register('ndt-method-qualification', NdtMethodQualificationOfNdtOperatorsView,
                basename='NdtMethodQualificationOfNdtOperators')
router.register('evidence-available', EvidenceAvailableOfCompletingPdcaView,
                basename='EvidenceAvailableOfCompletingPdca')
router.register('does-the-organisation-have', DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsView,
                basename='DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds')
router.register('are-results-always-discussed', AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamView,
                basename='AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam')
router.register('are-training-requirements', AretrainingrequirementsforrbiteammembersconsistentlyusedView,
                basename='Aretrainingrequirementsforrbiteammembersconsistentlyused')
router.register('does-the-item-valuation', DoesTheItemEvaluationHaveSignificantPittingView,
                basename='DoesTheItemEvaluationHaveSignificantPittingView')
router.register('can-the-degradation', CanTheDegradationMechanismBeRegardedAsLinearView,
                basename='CanTheDegradationMechanismBeRegardedAsLinear')
router.register('is-the-construction', IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationView,
                basename='IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationView')
router.register('are-procedures-in-place', AreProceduresInPlaceToPreventWaterContactView,
                basename='AreProceduresInPlaceToPreventWaterContact')
router.register('is-the-corrosion-rate-determined', IsTheCorrosionRateDeterminedWithAtLeast2SourcesView,
                basename='IsTheCorrosionRateDeterminedWithAtLeast2Sources')
router.register('is-the-degradation-speed-calculated', IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsView,
                basename='IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints')
router.register('which-method-is-used', WhichMethodIsUsedView,
                basename='WhichMethodIsUsed')


urlpatterns = [
    path('', include(router.urls))
]
