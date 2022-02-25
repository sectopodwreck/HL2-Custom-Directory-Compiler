"""
Default Keyvals for HL2 manifest files.

All methods return a dictionary of dictionary of arrays.
"""

import vkvParser as vkv

HL2_GAME_DEFAULT = [
    "scripts/game_sounds.txt",
    "scripts/game_sounds_ui.txt",
    "scripts/game_sounds_player.txt",
    "scripts/game_sounds_weapons.txt",
    "scripts/game_sounds_world.txt",
    "scripts/game_sounds_ambient_generic.txt",
    "scripts/game_sounds_items.txt",
    "scripts/game_sounds_physics.txt",
    "scripts/game_sounds_vehicles.txt",
    "scripts/level_sounds_e3_c17.txt",
    "scripts/level_sounds_e3_town.txt",
    "scripts/level_sounds_e3_bugbait.txt",
    "scripts/level_sounds_eli_lab.txt",
    "scripts/level_sounds_trainyard.txt",
    "scripts/level_sounds_k_lab.txt",
    "scripts/level_sounds_k_lab2.txt",
    "scripts/level_sounds_coast.txt",
    "scripts/level_sounds_novaprospekt.txt",
    "scripts/level_sounds_streetwar.txt",
    "scripts/level_sounds_streetwar2.txt",
    "scripts/level_sounds_breencast.txt",
    "scripts/level_sounds_citadel.txt",
    "scripts/level_sounds_canals.txt",
    "scripts/level_sounds_ravenholm.txt",
    "scripts/level_sounds_ravenholm2.txt",
    "scripts/level_sounds_canals2.txt",
    "scripts/level_sounds_music.txt",
    "scripts/npc_sounds_eli.txt",
    "scripts/npc_sounds_alyx.txt",
    "scripts/npc_sounds_dog.txt",
    "scripts/npc_sounds_citizen.txt",
    "scripts/npc_sounds_barney.txt",
    "scripts/npc_sounds_soldier.txt",
    "scripts/npc_sounds_strider.txt",
    "scripts/npc_sounds_zombie.txt",
    "scripts/npc_sounds_vortigaunt.txt",
    "scripts/npc_sounds_turret.txt",
    "scripts/npc_sounds_scanner.txt",
    "scripts/npc_sounds_rollermine.txt",
    "scripts/npc_sounds_poisonzombie.txt",
    "scripts/npc_sounds_metropolice.txt",
    "scripts/npc_sounds_combinecamera.txt",
    "scripts/npc_sounds_manhack.txt",
    "scripts/npc_sounds_ichthyosaur.txt",
    "scripts/npc_sounds_blackheadcrab.txt",
    "scripts/npc_sounds_fastheadcrab.txt",
    "scripts/npc_sounds_headcrab.txt",
    "scripts/npc_sounds_fastzombie.txt",
    "scripts/npc_sounds_birds.txt",
    "scripts/npc_sounds_gunship.txt",
    "scripts/npc_sounds_dropship.txt",
    "scripts/npc_sounds_barnacle.txt",
    "scripts/npc_sounds_attackheli.txt",
    "scripts/npc_sounds_antlionguard.txt",
    "scripts/npc_sounds_antlion.txt",
    "scripts/npc_sounds_env_headcrabcanister.txt",
    "scripts/npc_sounds_combine_ball.txt",
    "scripts/npc_sounds_combine_mine.txt",
    "scripts/npc_sounds_sniper.txt",
    "scripts/npc_sounds_stalker.txt",
    "scripts/npc_sounds_gman.txt"
]

HL2_PARTICLE_DEFAULT = [
    "particles/error.pcf",
    "particles/antlion_blood.pcf",
    "particles/blood_impact.pcf",
    "particles/water_impact.pcf",
    "particles/fire_01.pcf",
    "particles/burning_fx.pcf",
    "particles/combineball.pcf",
    "particles/vortigaunt_fx.pcf",
    "particles/rocket_fx.pcf"
]

HL2_SOUNDSCAPE_DEFAULT = [
    "scripts/soundscapes.txt",
    "scripts/soundscapes_canals.txt",
    "scripts/soundscapes_klab.txt",
    "scripts/soundscapes_elab.txt",
    "scripts/soundscapes_streetwar.txt",
    "scripts/soundscapes_citadel.txt",
    "scripts/soundscapes_town.txt",
    "scripts/soundscapes_coast.txt",
    "scripts/soundscapes_prison.txt",
    "scripts/soundscapes_trainyard.txt"
]

HL2_SURFACEPROP_DEFAULT = [
    "scripts/surfaceproperties.txt",
    "scripts/surfaceproperties_hl2.txt"
]

EPISODIC_GAME_DEFAULT = [
    "scripts/npc_sounds_alyx_episodic.txt",
    "scripts/npc_sounds_strider_episodic.txt",
    "scripts/npc_sounds_turret_episodic.txt",
    "scripts/npc_sounds_soldier_episodic.txt",
    "scripts/npc_sounds_ministrider_episodic.txt",
    "scripts/npc_sounds_roller_episodic.txt",
    "scripts/npc_sounds_combine_ball_episodic.txt",
    "scripts/npc_sounds_citizen_episodic.txt",
    "scripts/npc_sounds_citizen_ep1.txt",
    "scripts/npc_sounds_zombine.txt",
    "scripts/npc_sounds_dog_episodic.txt",
    "scripts/npc_sounds_antlion_episodic.txt",
    "scripts/npc_sounds_antlionguard_episodic.txt",
    "scripts/npc_sounds_advisor.txt",
    "scripts/level_sounds_music_episodic.txt",
    "scripts/game_sounds_weapons_episodic.txt",
    "scripts/level_voices_episode_01.txt",
    "scripts/level_sounds_aftermath_episodic.txt",
    "scripts/level_sounds_outland_episodic.txt",
    "scripts/level_sounds_c17_02a.txt",
    "scripts/level_voices_episode_02.txt"
]

EPISODIC_PARTICLE_DEFAULT = [
    "particles/ep1_fx.pcf"
]

EPISODIC_SOUNDSCAPE_DEFAULT = [
    "scripts/soundscapes_lostcoast.txt",
    "scripts/soundscapes_citadel_episodic.txt",
    "scripts/soundscapes_city_episodic.txt"
]

EP2_GAME_DEFAULT = [
    "scripts/game_sounds_weapons_ep2.txt",
    "scripts/npc_sounds_strider_episodic2.txt",
    "scripts/npc_sounds_citizen_episodic2.txt",
    "scripts/npc_sounds_antlionguard_episodic2.txt",
    "scripts/npc_sounds_advisor_episodic2.txt",
    "scripts/npc_sounds_hunter.txt",
    "scripts/npc_sounds_antlion_grub_episodic.txt",
    "scripts/npc_sounds_attackheli_episodic2.txt",
    "scripts/npc_sounds_fastzombie_episodic2.txt",
    "scripts/game_sounds_addendum_ep2.txt",
    "scripts/level_sounds_music_episodic2.txt",
    "scripts/game_sounds_vehicles_ep2.txt",
    "scripts/game_sounds_physics_ep2.txt",
    "scripts/npc_sounds_combine_cannon.txt",
    "scripts/npc_sounds_alyx_episodic2.txt",
    "scripts/npc_sounds_turret_episodic2.txt"
]

EP2_PARTICLE_DEFAULT = [
    "particles/explosion.pcf",
    "particles/vehicle.pcf",
    "particles/dust_bombdrop.pcf",
    "particles/building_explosion.pcf",
    "particles/antlion_gib_01.pcf",
    "particles/antlion_gib_02.pcf",
    "particles/stalactite.pcf",
    "particles/striderbuster.pcf",
    "particles/door_explosion.pcf",
    "particles/choreo_launch.pcf",
    "particles/water_leaks.pcf",
    "particles/antlion_worker.pcf",
    "particles/skybox_smoke.pcf",
    "particles/waterfall.pcf",
    "particles/aurora.pcf",
    "particles/rain.pcf",
    "particles/warpshield.pcf",
    "particles/aurora_sphere2.pcf",
    "particles/advisor.pcf",
    "particles/hunter_shield_impact.pcf",
    "particles/hunter_intro.pcf",
    "particles/dust_rumble.pcf",
    "particles/Advisor_FX.pcf",
    "particles/hunter_projectile.pcf",
    "particles/choreo_dog_v_strider.pcf",
    "particles/steampuff.pcf",
    "particles/magnusson_burner.pcf",
    "particles/waterdrips.pcf",
    "particles/hunter_flechette.pcf",
    "particles/choreo_gman.pcf",
    "particles/weapon_fx.pcf",
    "particles/choreo_extract.pcf",
    "particles/devtest.pcf",
    "particles/electrical_fx.pcf",
    "particles/grub_blood.pcf",
    "particles/grenade_fx.pcf",
    "particles/impact_fx.pcf"
]

EP2_SOUNDSCAPE_DEFAULT = [
    "scripts/soundscapes_silo.txt",
    "scripts/soundscapes_outland.txt",
    "scripts/soundscapes_outland2.txt"
]

EP2_SURFACEPROP_DEFAULT = [
    "scripts/surfaceproperties_ep2.txt"
]

"""
Initalize a generic manifest.
"""
def initManifest(strKey):
    return {strKey: {}}

"""
    HL2 Defaults.
"""

def hl2GetGameSounds():
    dictManifest = initManifest("game_sounds_manifest")
    dictManifest["game_sounds_manifest"]["precache_file"] = HL2_GAME_DEFAULT.copy()
    
    return dictManifest

def hl2GetParticles():
    dictManifest = initManifest("particles_manifest")
    dictManifest["particles_manifest"]["file"] = HL2_PARTICLE_DEFAULT.copy()

    return dictManifest

def hl2GetSoundscapes():
    dictManifest = initManifest("soundscaples_manifest")
    dictManifest["soundscaples_manifest"]["file"] = HL2_SOUNDSCAPE_DEFAULT.copy()

    return dictManifest

def hl2GetSurfaceprops():
    dictManifest = initManifest("surfaceproperties_manifest")
    dictManifest["surfaceproperties_manifest"]["file"] = HL2_SURFACEPROP_DEFAULT.copy()

    return dictManifest

"""
    EP1 Defaults.
"""

def episodicGetGameSounds():
    dictManifest = hl2GetGameSounds()
    dictManifest["game_sounds_manifest"]["precache_file"] += EPISODIC_GAME_DEFAULT

    return dictManifest

def episodicGetParticles():
    dictManifest = hl2GetParticles()
    dictManifest["particles_manifest"]["file"] += EPISODIC_PARTICLE_DEFAULT
    
    return dictManifest

def episodicGetSoundscapes():
    dictManifest = hl2GetSoundscapes()
    dictManifest["soundscaples_manifest"]["file"] += EPISODIC_SOUNDSCAPE_DEFAULT

    return dictManifest

"""
    EP2 Defaults.
"""

def ep2GetGameSounds():
    dictManifest = episodicGetGameSounds()
    dictManifest["game_sounds_manifest"]["precache_file"] += EP2_GAME_DEFAULT

    return dictManifest

def ep2GetParticles():
    dictManifest = episodicGetParticles()
    dictManifest["particles_manifest"]["file"] += EP2_PARTICLE_DEFAULT

    return dictManifest

def ep2GetSoundscapes():
    dictManifest = episodicGetSoundscapes()
    dictManifest["soundscaples_manifest"]["file"] += EP2_SOUNDSCAPE_DEFAULT

    return dictManifest

def ep2GetSurfaceprops():
    dictManifest = hl2GetSurfaceprops()
    dictManifest["surfaceproperties_manifest"]["file"] += EP2_SURFACEPROP_DEFAULT

    return dictManifest
