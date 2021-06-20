from rest_framework import serializers

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
    Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed,
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


def formatScore(name):
    return name.split('- S')[0].strip()


def formatName(name):
    return name.split('-')[0].strip()
    # name = name.split('-')
    # if len(name) > 2:
        # return '-'.join(name[:2])
    # return name[0].strip()



class NameFormatting:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = formatName(instance.name)
        return data


class ImpressCathodicProtectionSerializer(
    NameFormatting,
    serializers.ModelSerializer):

    class Meta:
        model = ImpressCathodicProtection
        fields = ['id', 'name']


class SacrificialCathodicPropectionSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = SacrificialCathodicPropection
        fields = ['id', 'name']



class BottomPlatesInternalCoatingLiningSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = BottomPlatesInternalCoatingLining
        fields = ['id', 'name']




class BottomPlatesExternalCoatingSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = BottomPlatesExternalCoating
        fields = ['id', 'name']


class StorageConditionsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = StorageConditions
        fields = ['id', 'name']



class TypeOfBottomSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = TypeOfBottom
        fields = ['id', 'name']


class HeatingCoilsInTankSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = HeatingCoilsInTank
        fields = ['id', 'name']



class ProductCorrosivitySerializer(
    # NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProductCorrosivity
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = formatScore(instance.name)
        return data


class FoundationTypeSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = FoundationType
        fields = ['id', 'name']



class HeightOfFoundationSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = HeightOfFoundation
        fields = ['id', 'name']


class EffectivenessOfDrainageSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = EffectivenessOfDrainage
        fields = ['id', 'name']


class TimeToRepairSerializer(
    serializers.ModelSerializer):
    class Meta:
        model = TimeToRepair
        fields = ['id', 'name']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = formatScore(instance.name)
        return data


class CostOfRepairSerializer(
    # NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = CostOfRepair
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = formatScore(instance.name)
        return data





class ProbableMagnitudeOfProductLossSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProbableMagnitudeOfProductLoss
        fields = ['id', 'name']


class LikelihoodOfInjuryToPersonnelSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = LikelihoodOfInjuryToPersonnel
        fields = ['id', 'name']



class ProductFlammabilityAsPerMCSPSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProductFlammabilityAsPerMCSP
        fields = ['id', 'name']


class ProductToxicitySerializer(
    serializers.ModelSerializer):
    class Meta:
        model = ProductToxicity
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = formatScore(instance.name)
        return data



class LocationOfTankFarmSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = LocationOfTankFarm
        fields = ['id', 'name']


class TankLocatedNearPublicFenceSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = TankLocatedNearPublicFence
        fields = ['id', 'name']


class EnvironmetalHazardToSoilAndWaterSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = EnvironmetalHazardToSoilAndWater
        fields = ['id', 'name']



class VapourEmissionSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = VapourEmission
        fields = ['id', 'name']


class AccelerationFactorForPittingSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = AccelerationFactorForPitting
        fields = ['id', 'name']



class NDTMethodUsedForThicknessMeasurementsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = NDTMethodUsedForThicknessMeasurements
        fields = ['id', 'name']



class FrequencyOfInternalInspectionsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = FrequencyOfInternalInspections
        fields = ['id', 'name']


class NdtMethodQualificationOfNdtOperatorsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = Ndt_Method_And_Qualification_Of_Ndt_Operators_In_Place_And_Assessed
        fields = ['id', 'name']


class EvidenceAvailableOfCompletingPdcaSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = EvidenceAvailableOfCompletingPdca
        fields = ['id', 'name']


class DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeedsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = DoesTheOrganisationHaveTheProperQualificationsToDetermineDegradationsSpeeds
        fields = ['id', 'name']


class AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeamSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = AreResultsAlwaysDiscussedInAMultidisciplinaryRbiTeam
        fields = ['id', 'name']


class AretrainingrequirementsforrbiteammembersconsistentlyusedSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = Aretrainingrequirementsforrbiteammembersconsistentlyused
        fields = ['id', 'name']


class DoesTheItemEvaluationHaveSignificantPittingSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = DoesTheItemEvaluationHaveSignificantPitting
        fields = ['id', 'name']


class CanTheDegradationMechanismBeRegardedAsLinearSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = CanTheDegradationMechanismBeRegardedAsLinear
        fields = ['id', 'name']


class IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfigurationSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = IsTheConstructionSuchThatCorrosionMayBeReducedByTheChosenWeldConfiguration
        fields = ['id', 'name']


class AreProceduresInPlaceToPreventWaterContactSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = AreProceduresInPlaceToPreventWaterContact
        fields = ['id', 'name']


class IsTheCorrosionRateDeterminedWithAtLeast2SourcesSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = IsTheCorrosionRateDeterminedWithAtLeast2Sources
        fields = ['id', 'name']


class IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPointsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = IsTheDegradationSpeedCalculatedByUsingAtLeast3MeasurementPoints
        fields = ['id', 'name']

class WhichMethodIsUsedSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = WhichMethodIsUsed
        fields = ['id', 'name']
