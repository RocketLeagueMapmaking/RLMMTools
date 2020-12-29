class UDKObject():
    def __init__(self, objclass):
        self.objclass = objclass
        self.name = self.objclass + "_0"

        self.ArchetypeDict = {
            "StaticMeshActor": {
                "ActorClass": "StaticMeshActor",
                "ActorName": "StaticMeshActor_0",
                "ActorArchetype": "StaticMeshActor'Engine.Default__StaticMeshActor'",
                "ObjectClass": "StaticMeshComponent",
                "ObjectName": "StaticMeshComponent0",
                "ObjectObjName": "StaticMeshComponent_0",
                "ObjectArchetype": "StaticMeshComponent'Engine.Default__StaticMeshActor:StaticMeshComponent0'"
            },
            "VehiclePickup_Boost_Pill": {
                "ActorClass": "VehiclePickup_Boost_TA",
                "ActorName": "VehiclePickup_Boost_TA_0",
                "ActorArchetype": "VehiclePickup_Boost_TA'HoopsStadium_P.archetypes.vehiclepickup.VehiclePickup_BoostPill'",
                "ObjectClass": "SpriteComponent",
                "ObjectName": "Sprite",
                "ObjectObjName": "SpriteComponent_0",
                "ObjectArchetype": "SpriteComponent'HoopsStadium_P.archetypes.vehiclepickup.VehiclePickup_BoostPill:Sprite'"
            },
            "FXActor_Boost_Pill": {
                "ActorClass": "FXActor_TA",
                "ActorName": "FXActor_TA_0",
                "ActorArchetype": "FXActor_TA'Park_P.pickup_boost.BoostPill_FXActor'",
                "ObjectClass": "ParameterDispenser_X",
                "ObjectName": "DefaultParameters",
                "ObjectObjName": "ParameterDispenser_X_8",
                "ObjectArchetype": "ParameterDispenser_X'Park_P.pickup_boost.BoostPill_FXActor:DefaultParameters'"
            },
            "VehiclePickup_Boost_Pad": {
                "ActorClass": "VehiclePickup_Boost_TA",
                "ActorName": "VehiclePickup_Boost_TA_0",
                "ActorArchetype": "VehiclePickup_Boost_TA'tagame.Default__VehiclePickup_Boost_TA'",
                "ObjectClass": "SpriteComponent",
                "ObjectName": "Sprite",
                "ObjectObjName": "SpriteComponent_0",
                "ObjectArchetype": "SpriteComponent'tagame.Default__VehiclePickup_Boost_TA:Sprite'"
            },
            "FXActor_Boost_Pad": {
                "ActorClass": "FXActor_TA",
                "ActorName": "FXActor_TA_0",
                "ActorArchetype": "FXActor_TA'Park_P.pickup_boost.BoostPad_FXActor'",
                "ObjectClass": "ParameterDispenser_X",
                "ObjectName": "DefaultParameters",
                "ObjectObjName": "ParameterDispenser_X_0",
                "ObjectArchetype": "ParameterDispenser_X'Park_P.pickup_boost.BoostPad_FXActor:DefaultParameters'"
            }
        }

        self.actorattributes = {}
        self.objectattributes = {}


    def renderText(self):
        lines = []
        lines[0] = "Begin Map"
        lines[1] = "Begin Level"

        lines[2] = "Begin Actor"
        lines[2] += " Class=" + self.ArchetypeDict[self.objclass]["ActorClass"]
        lines[2] += " Name=" + self.ArchetypeDict[self.objclass]["ActorName"]
        lines[2] += " Archetype=" + self.ArchetypeDict[self.objclass]["ActorArchetype"]

