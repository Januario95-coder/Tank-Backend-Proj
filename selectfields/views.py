from rest_framework.viewsets import ModelViewSet

from selectfields.serializers import (
    ImpressCathodicProtectionSerializer,
    SacrificialCathodicPropectionSerializer,
    BottomPlatesInternalCoatingLiningSerializer,
    BottomPlatesExternalCoatingSerializer,
    StorageConditionsSerializer,
    TypeOfBottomSerializer,
    HeatingCoilsInTankSerializer,
    ProductCorrosivitySerializer,
    FoundationTypeSerializer,
    HeightOfFoundationSerializer,
    EffectivenessOfDrainageSerializer,
    TimeToRepairSerializer,
    CostOfRepairSerializer,
    ProbableMagnitudeOfProductLossSerializer,
    LikelihoodOfInjuryToPersonnelSerializer,
    ProductFlammabilityAsPerMCSPSerializer,
    ProductToxicitySerializer,
    LocationOfTankFarmSerializer,
    TankLocatedNearPublicFenceSerializer,
    EnvironmetalHazardToSoilAndWaterSerializer,
    VapourEmissionSerializer,
    AccelerationFactorForPittingSerializer,
    NDTMethodUsedForThicknessMeasurementsSerializer,
    FrequencyOfInternalInspectionsSerializer,
    Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed,
    NdtMethodQualificationOfNdtOperatorsSerializer,
    EvidenceAvailableOfCompletingPdcaSerializer,
    DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsSerializer,
    AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamSerializer,
    AretrainingrequirementsforrbiteammembersconsistentlyusedSerializer,
    DoesTheItemEvaluationHaveSignificantPittingSerializer,
    CanTheDegradationMechanismBeRegardedAsLinearSerializer,
    IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationSerializer,

    AreProceduresInPlaceToPreventWaterContactSerializer,
    IsTheCorrosionRateDeterminedWithAtLeast2SourcesSerializer,
    IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsSerializer,
    WhichMethodIsUsedSerializer
)


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
    TankLocatedNearPublicFence,
    EnvironmetalHazardToSoilAndWater,
    VapourEmission,
    AccelerationFactorForPitting,
    NDTMethodUsedForThicknessMeasurements,
    FrequencyOfInternalInspections,
    EvidenceAvailableOfCompletingPdca,
    DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds,
    AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam,
    Aretrainingrequirementsforrbiteammembersconsistentlyused,
    DoesTheItemEvaluationHaveSignificantPitting,
    CanTheDegradationMechanismBeRegardedAsLinear,
    IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration,

    AreProceduresInPlaceToPreventWaterContact,
    IsTheCorrosionRateDeterminedWithAtLeast2Sources,
    IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints,
    WhichMethodIsUsed
)



class ImpressCathodicProtectionView(ModelViewSet):
    serializer_class = ImpressCathodicProtectionSerializer
    queryset = ImpressCathodicProtection.objects.all()



class SacrificialCathodicPropectionView(ModelViewSet):
    serializer_class = SacrificialCathodicPropectionSerializer
    queryset = SacrificialCathodicPropection.objects.all()


class BottomPlatesInternalCoatingLiningView(ModelViewSet):
    serializer_class = BottomPlatesInternalCoatingLiningSerializer
    queryset = BottomPlatesInternalCoatingLining.objects.all()


class BottomPlatesExternalCoatingView(ModelViewSet):
    serializer_class = BottomPlatesExternalCoatingSerializer
    queryset = BottomPlatesExternalCoating.objects.all()


class StorageConditionsView(ModelViewSet):
    serializer_class = StorageConditionsSerializer
    queryset = StorageConditions.objects.all()


class TypeOfBottomView(ModelViewSet):
    serializer_class = TypeOfBottomSerializer
    queryset = TypeOfBottom.objects.all()


class HeatingCoilsInTankView(ModelViewSet):
    serializer_class = HeatingCoilsInTankSerializer
    queryset = HeatingCoilsInTank.objects.all()


class ProductCorrosivityView(ModelViewSet):
    serializer_class = ProductCorrosivitySerializer
    queryset = ProductCorrosivity.objects.all()


class FoundationTypeView(ModelViewSet):
    serializer_class = FoundationTypeSerializer
    queryset = FoundationType.objects.all()


class HeightOfFoundationView(ModelViewSet):
    serializer_class = HeightOfFoundationSerializer
    queryset = HeightOfFoundation.objects.all()


class EffectivenessOfDrainageView(ModelViewSet):
    serializer_class = EffectivenessOfDrainageSerializer
    queryset = EffectivenessOfDrainage.objects.all()


class TimeToRepairView(ModelViewSet):
    serializer_class = TimeToRepairSerializer
    queryset = TimeToRepair.objects.all()


class CostOfRepairView(ModelViewSet):
    serializer_class = CostOfRepairSerializer
    queryset = CostOfRepair.objects.all()


class ProbableMagnitudeOfProductLossView(ModelViewSet):
    serializer_class = ProbableMagnitudeOfProductLossSerializer
    queryset = ProbableMagnitudeOfProductLoss.objects.all()


class LikelihoodOfInjuryToPersonnelView(ModelViewSet):
    serializer_class = LikelihoodOfInjuryToPersonnelSerializer
    queryset = LikelihoodOfInjuryToPersonnel.objects.all()



class ProductFlammabilityAsPerMCSPView(ModelViewSet):
    serializer_class = ProductFlammabilityAsPerMCSPSerializer
    queryset = ProductFlammabilityAsPerMCSP.objects.all()


class ProductToxicityView(ModelViewSet):
    serializer_class = ProductToxicitySerializer
    queryset = ProductToxicity.objects.all()


class LocationOfTankFarmView(ModelViewSet):
    serializer_class = LocationOfTankFarmSerializer
    queryset = LocationOfTankFarm.objects.all()


class TankLocatedNearPublicFenceView(ModelViewSet):
    serializer_class = TankLocatedNearPublicFenceSerializer
    queryset = TankLocatedNearPublicFence.objects.all()


class EnvironmetalHazardToSoilAndWaterView(ModelViewSet):
    serializer_class = EnvironmetalHazardToSoilAndWaterSerializer
    queryset = EnvironmetalHazardToSoilAndWater.objects.all()


class VapourEmissionView(ModelViewSet):
    serializer_class = VapourEmissionSerializer
    queryset = VapourEmission.objects.all()


class AccelerationFactorForPittingView(ModelViewSet):
    serializer_class = AccelerationFactorForPittingSerializer
    queryset = AccelerationFactorForPitting.objects.all()


class NDTMethodUsedForThicknessMeasurementsView(ModelViewSet):
    serializer_class = NDTMethodUsedForThicknessMeasurementsSerializer
    queryset = NDTMethodUsedForThicknessMeasurements.objects.all()


class FrequencyOfInternalInspectionsView(ModelViewSet):
    serializer_class = FrequencyOfInternalInspectionsSerializer
    queryset = FrequencyOfInternalInspections.objects.all()


class NdtMethodQualificationOfNdtOperatorsView(ModelViewSet):
    serializer_class = NdtMethodQualificationOfNdtOperatorsSerializer
    queryset = Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed.objects.all()


class EvidenceAvailableOfCompletingPdcaView(ModelViewSet):
    serializer_class = EvidenceAvailableOfCompletingPdcaSerializer
    queryset = EvidenceAvailableOfCompletingPdca.objects.all()


class DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsView(ModelViewSet):
    serializer_class = DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsSerializer
    queryset = DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds.objects.all()


class AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamView(ModelViewSet):
    serializer_class = AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamSerializer
    queryset = AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam.objects.all()

class AretrainingrequirementsforrbiteammembersconsistentlyusedView(ModelViewSet):
    serializer_class = AretrainingrequirementsforrbiteammembersconsistentlyusedSerializer
    queryset = Aretrainingrequirementsforrbiteammembersconsistentlyused.objects.all()


class DoesTheItemEvaluationHaveSignificantPittingView(ModelViewSet):
    serializer_class = DoesTheItemEvaluationHaveSignificantPittingSerializer
    queryset = DoesTheItemEvaluationHaveSignificantPitting.objects.all()



class CanTheDegradationMechanismBeRegardedAsLinearView(ModelViewSet):
    serializer_class = CanTheDegradationMechanismBeRegardedAsLinearSerializer
    queryset = CanTheDegradationMechanismBeRegardedAsLinear.objects.all()


class IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationView(ModelViewSet):
    serializer_class = IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationSerializer
    queryset = IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration.objects.all()


class AreProceduresInPlaceToPreventWaterContactView(ModelViewSet):
    serializer_class = AreProceduresInPlaceToPreventWaterContactSerializer
    queryset = AreProceduresInPlaceToPreventWaterContact.objects.all()


class IsTheCorrosionRateDeterminedWithAtLeast2SourcesView(ModelViewSet):
    serializer_class = IsTheCorrosionRateDeterminedWithAtLeast2SourcesSerializer
    queryset = IsTheCorrosionRateDeterminedWithAtLeast2Sources.objects.all()


class IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsView(ModelViewSet):
    serializer_class = IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsSerializer
    queryset = IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints.objects.all()


class WhichMethodIsUsedView(ModelViewSet):
    serializer_class = WhichMethodIsUsedSerializer
    queryset = WhichMethodIsUsed.objects.all()
