from django.contrib import admin

from .models import (
    ImpressCathodicProtection,
    SacrificialCathodicPropection,
    BottomPlatesInternalCoatingLining,
    BottomPlatesExternalCoating,
    StorageConditions,
    TypeOfBottom,
    HeatingCoilsInTank,
    ProductCorrosivity,
    FoundationType,
    HeightOfFoundation,
    EffectivenessOfDrainage,
    TimeToRepair,
    CostOfRepair,
    ProbableMagnitudeOfProductLoss,
    LikelihoodOfInjuryToPersonnel,
    ProductFlammabilityAsPerMCSP,
    ProductToxicity,
    LocationOfTankFarm,
    EnvironmetalHazardToSoilAndWater,
    AccelerationFactorForPitting,
    VapourEmission,
    NDTMethodUsedForThicknessMeasurements,
    FrequencyOfInternalInspections,
    Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed,
    EvidenceAvailableOfCompletingPdca,
    DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds,
    AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam,
    Aretrainingrequirementsforrbiteammembersconsistentlyused,
    DoesTheItemEvaluationHaveSignificantPitting,
    CanTheDegradationMechanismBeRegardedAsLinear,
    IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration,

    IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration,

    AreProceduresInPlaceToPreventWaterContact,
    IsTheCorrosionRateDeterminedWithAtLeast2Sources,
    IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints,
    WhichMethodIsUsed
)


@admin.register(ImpressCathodicProtection)
class ImpressCathodicProtectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(SacrificialCathodicPropection)
class SacrificialCathodicPropectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(BottomPlatesInternalCoatingLining)
class BottomPlatesInternalCoatingLiningAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(BottomPlatesExternalCoating)
class BottomPlatesExternalCoatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(StorageConditions)
class StorageConditionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(TypeOfBottom)
class TypeOfBottomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(HeatingCoilsInTank)
class HeatingCoilsInTankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(ProductCorrosivity)
class ProductCorrosivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score']
    ordering = ['id']

    def score(self, obj):
        return obj.name.split('=')[-1]

    score.short_description = 'Score value'


@admin.register(FoundationType)
class FoundationTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(HeightOfFoundation)
class HeightOfFoundationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(EffectivenessOfDrainage)
class EffectivenessOfDrainageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(TimeToRepair)
class TimeToRepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(CostOfRepair)
class CostOfRepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(ProbableMagnitudeOfProductLoss)
class ProbableMagnitudeOfProductLossAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(LikelihoodOfInjuryToPersonnel)
class LikelihoodOfInjuryToPersonnelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(ProductFlammabilityAsPerMCSP)
class ProductFlammabilityAsPerMCSPAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(ProductToxicity)
class ProductToxicityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score']
    ordering = ['id']

    def score(self, obj):
        return obj.name.split('=')[-1]

    score.short_description = 'Score value'


@admin.register(LocationOfTankFarm)
class LocationOfTankFarmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(EnvironmetalHazardToSoilAndWater)
class EnvironmetalHazardToSoilAndWaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(AccelerationFactorForPitting)
class AccelerationFactorForPittingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(VapourEmission)
class VapourEmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(NDTMethodUsedForThicknessMeasurements)
class NDTMethodUsedForThicknessMeasurementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(FrequencyOfInternalInspections)
class FrequencyOfInternalInspectionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed)
class NdtMethodQualificationOfNdtOperatorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(EvidenceAvailableOfCompletingPdca)
class EvidenceAvailableOfCompletingPdcaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds)
class DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam)
class AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(Aretrainingrequirementsforrbiteammembersconsistentlyused)
class AretrainingrequirementsforrbiteammembersconsistentlyusedAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(DoesTheItemEvaluationHaveSignificantPitting)
class DoesTheItemEvaluationHaveSignificantPittingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(CanTheDegradationMechanismBeRegardedAsLinear)
class CanTheDegradationMechanismBeRegardedAsLinearAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration)
class IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(AreProceduresInPlaceToPreventWaterContact)
class AreProceduresInPlaceToPreventWaterContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(IsTheCorrosionRateDeterminedWithAtLeast2Sources)
class IsTheCorrosionRateDeterminedWithAtLeast2SourcesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints)
class IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(WhichMethodIsUsed)
class WhichMethodIsUsedAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
