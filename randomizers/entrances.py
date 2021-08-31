
from data.entrances import *
import wwr_ui.entrances as uie
from collections import OrderedDict, namedtuple

catDict = OrderedDict()
catDict["dungeon"] = OrderedDict([("Entrances",DUNGEON_ENTRANCES),("Exits",DUNGEON_EXITS),("IxRequirement",DUNGEON_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS),("OxRequirement",DUNGEON_EXIT_NAMES_WITH_NO_REQUIREMENTS),("Setting","progression_dungeons")])
catDict["fairy"] = OrderedDict([("Entrances",FAIRY_ENTRANCES),("Exits",FAIRY_EXITS),("IxRequirement",FAIRY_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS),("OxRequirement",FAIRY_EXIT_NAMES_WITH_NO_REQUIREMENTS),("Setting","progression_great_fairies")])
catDict["puzzle"] = OrderedDict([("Entrances",PUZZLE_CAVE_ENTRANCES),("Exits",PUZZLE_CAVE_EXITS),("IxRequirement",PUZZLE_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS),("OxRequirement",PUZZLE_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS),("Setting","progression_puzzle_secret_caves")])
catDict["mixed"] = OrderedDict([("Entrances",MIXED_CAVE_ENTRANCES),("Exits",MIXED_CAVE_EXITS),("IxRequirement",MIXED_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS),("OxRequirement",MIXED_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS),("Setting","progression_mixed_secret_caves")])
catDict["combat"] = OrderedDict([("Entrances",COMBAT_CAVE_ENTRANCES),("Exits",COMBAT_CAVE_EXITS),("IxRequirement",COMBAT_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS),("OxRequirement",COMBAT_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS),("Setting","progression_combat_secret_caves")])
catTuple = namedtuple("catTuple",["name", "vanilla", "group", "children"])
class catTuple:
  def __init__(self,name:str,vanilla:bool,group:str,children,*args):
    self.name = name
    self.vanilla = vanilla
    self.group = group
    self.children = children
    self.kids = self.children
    self.aux = args

  def __str__(self):
    return "-----\n{name}:\n  Vanilla: {vanilla}\n  Group: {group}\n  Children: {children}\n-----".format(name=self.name,vanilla=self.vanilla,group=self.group,children=self.children)


# TODO: Maybe make a separate list of entrances and exits that have no requirements when you start with a sword. (e.g. Cliff Plateau Isles Floating Plants Cave.) Probably not necessary though.

def randomize_entrances(self):
  entrance_cats = OrderedDict()
  entrance_cats["Dungeon Entrances"] = catTuple("dungeon", True, "v", None)
  entrance_cats["Fairy Fountain Entrances"] = catTuple("fairy", True, "v", None)
  entrance_cats["Secret Cave Entrances - Puzzle"] = catTuple("puzzle", True, "v", None)
  entrance_cats["Secret Cave Entrances - Mixed"] = catTuple("mixed", True, "v", None)
  entrance_cats["Secret Cave Entrances - Combat"] = catTuple("combat", True, "v", None)
  child_cave_prog = ["Secret Cave Entrances - Puzzle"] * self.options.get("progression_puzzle_secret_caves") + ["Secret Cave Entrances - Mixed"] * self.options.get("progression_mixed_secret_caves") + ["Secret Cave Entrances - Combat"] * self.options.get("progression_combat_secret_caves")
  cat_prog = catTuple("cave_prog", True, "v", child_cave_prog)
  entrance_cats["Secret Cave Entrances - Progression"] = cat_prog
  child_cave_notp = ["Secret Cave Entrances - Puzzle"] * (not self.options.get("progression_puzzle_secret_caves")) + ["Secret Cave Entrances - Mixed"] * (not self.options.get("progression_mixed_secret_caves")) + ["Secret Cave Entrances - Combat"] * (not self.options.get("progression_combat_secret_caves"))
  cat_notp = catTuple("cave_notp", True, "v", child_cave_notp)
  entrance_cats["Secret Cave Entrances - Not Progression"] = cat_notp

  full_entrances = self.options.get("full_entrances")
  full_entrances.sort(key=lambda x:uie.SORT_KEY_ENTRANCES.index(x)) # This doesn't matter but is helpful
  full_cats = []
  for cats in full_entrances:
    cat = entrance_cats[cats]
    cat.group = "f"
    cat.vanilla = False
    if cat.children:
      for child in cat.children:
        kid = entrance_cats[child]
        if child not in cats and kid.vanilla:
          kid.group = "f"
          kid.vanilla = False
          full_cats.append(kid)
          # No child has children at this time
    else:
      full_cats.append(cat)

  limited_entrances = self.options.get("limited_entrances")
  limited_entrances.sort(key=lambda x:uie.SORT_KEY_ENTRANCES.index(x)) # This is to ensure we know SCP and SCNP come before their children
  limited_cats = []
  for cats in limited_entrances:
    cat = entrance_cats[cats]
    if cat.vanilla:
      cat.group = "l"
      cat.vanilla = False
      if cat.children:
        for child in cat.children:
          kid = entrance_cats[child]
          if kid.vanilla or (kid.vanilla and child in cats):
            kid.group = "l"
            kid.vanilla = False
            # For prevention reasons, we don't add to the cat group as to shuffle them together
            # No child has children at this time
      limited_cats.append(cat)

  # This shouldn't happen but we want to ensure
  if cat_prog in full_cats:
    full_cats.remove(cave_prog)
  if cat_notp in full_cats:
    full_cats.remove(cave_notp)

  if full_cats:
    randomize_one_set_of_entrances(self,*full_cats)

  if limited_cats:
    for cats in limited_cats:
      if cats.children:
        kittens = []
        for kids in cats.children:
          kittens.append(entrance_cats[kids])
        randomize_one_set_of_entrances(self,*kittens)
        continue
      randomize_one_set_of_entrances(self,cats)


def randomize_one_set_of_entrances(self, *args):
  cats = args

  relevant_entrances = []
  remaining_exits = []
  no_require_entrances = []
  no_require_exits = []

  for cat in cats:
    relevant_entrances+=catDict[cat.name]["Entrances"]
    remaining_exits+=catDict[cat.name]["Exits"]
    no_require_entrances.append(catDict[cat.name]["IxRequirement"])
    no_require_exits.append(catDict[cat.name]["OxRequirement"])

  doing_progress_entrances_for_dungeons_and_caves_only_start = False
  if self.dungeons_and_caves_only_start:
    for cat in cats:
      if not catDict[cat.name]["Setting"]:
        continue
      if self.options.get(catDict[cat.name]["Setting"]):
        doing_progress_entrances_for_dungeons_and_caves_only_start = True
        break

  if self.options.get("race_mode"):
    # Move entrances that are on islands with multiple entrances to the start of the list.
    # This is because we need to prevent these islands from having multiple dungeons on them in Race Mode, and this can fail if they're not at the start of the list because it's possible for the only possibility left to be to put multiple dungeons on one island.
    entrances_not_on_unique_islands = []
    for zone_entrance in relevant_entrances:
      for other_zone_entrance in relevant_entrances:
        if other_zone_entrance.island_name == zone_entrance.island_name and other_zone_entrance != zone_entrance:
          entrances_not_on_unique_islands.append(zone_entrance)
          break
    for zone_entrance in entrances_not_on_unique_islands:
      relevant_entrances.remove(zone_entrance)
    relevant_entrances = entrances_not_on_unique_islands + relevant_entrances

  if doing_progress_entrances_for_dungeons_and_caves_only_start:
    # If the player can't access any locations at the start besides dungeon/cave entrances, we choose an entrance with no requirements that will be the first place the player goes.
    # We will make this entrance lead to a dungeon/cave with no requirements so the player can actually get an item at the start.
    possible_safety_entrances = [
      e for e in relevant_entrances
      if e.entrance_name in no_require_entrances
    ]
    safety_entrance = self.rng.choice(possible_safety_entrances)

    # In order to avoid using up all dungeons/caves with no requirements, we have to do this entrance first, so move it to the start of the array.
    relevant_entrances.remove(safety_entrance)
    relevant_entrances.insert(0, safety_entrance)

  done_entrances_to_exits = {}
  for zone_entrance in relevant_entrances:
    if doing_progress_entrances_for_dungeons_and_caves_only_start and zone_entrance == safety_entrance:
      possible_remaining_exits = [e for e in remaining_exits if e.unique_name in no_require_exits]
    else:
      possible_remaining_exits = remaining_exits

    # The below is debugging code for testing the caves with timers.
    #if zone_entrance.entrance_name == "Crater on Fire Mountain":
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name == "Ice Ring Isle Secret Cave"
    #  ]
    #elif zone_entrance.entrance_name == "Palsa on Ice Ring Isle":
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name == "Fire Mountain Secret Cave"
    #  ]
    #else:
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name not in ["Fire Mountain Secret Cave", "Ice Ring Isle Secret Cave"]
    #  ]

    if self.options.get("race_mode") != "Default" and self.race_mode_quest_marker_mode == "With Entrances":
      # Prevent two entrances on the same island both leading into dungeons (DRC and Pawprint each have two entrances).
      # This is because Race Mode's dungeon markers only tell you what island required dungeons are on, not which of the two entrances it's in. So if a required dungeon and a non-required dungeon were on the same island there would be no way to tell which is required.
      done_entrances_on_same_island_leading_to_a_dungeon = [
        entr for entr in done_entrances_to_exits
        if entr.island_name == zone_entrance.island_name
        and done_entrances_to_exits[entr] in DUNGEON_EXITS
      ]
      if done_entrances_on_same_island_leading_to_a_dungeon:
        possible_remaining_exits = [x for x in possible_remaining_exits if x not in DUNGEON_EXITS]

    zone_exit = self.rng.choice(possible_remaining_exits)
    remaining_exits.remove(zone_exit)

    self.entrance_connections[zone_entrance.entrance_name] = zone_exit.unique_name
    self.dungeon_and_cave_island_locations[zone_exit.zone_name] = zone_entrance.island_name
    done_entrances_to_exits[zone_entrance] = zone_exit

    if not self.dry_run:
      # Update the stage this entrance takes you into.
      entrance_dzr_path = "files/res/Stage/%s/Room%d.arc" % (zone_entrance.stage_name, zone_entrance.room_num)
      entrance_dzr = self.get_arc(entrance_dzr_path).get_file("room.dzr")
      entrance_scls = entrance_dzr.entries_by_type("SCLS")[zone_entrance.scls_exit_index]
      entrance_scls.dest_stage_name = zone_exit.stage_name
      entrance_scls.room_index = zone_exit.room_num
      entrance_scls.spawn_id = zone_exit.spawn_id
      entrance_scls.save_changes()

      # Update the DRI spawn to not have spawn type 5.
      # If the DRI entrance was connected to the TotG dungeon, then exiting TotG while riding KoRL would crash the game.
      entrance_spawns = entrance_dzr.entries_by_type("PLYR")
      for spawn in entrance_spawns:
        if spawn.spawn_id == zone_entrance.spawn_id:
          entrance_spawn = spawn
          break
      if entrance_spawn.spawn_type == 5:
        entrance_spawn.spawn_type = 1
        entrance_spawn.save_changes()

      # Update the entrance you're put at when leaving the dungeon.
      exit_dzr_path = "files/res/Stage/%s/Room%d.arc" % (zone_exit.stage_name, zone_exit.room_num)
      exit_dzr = self.get_arc(exit_dzr_path).get_file("room.dzr")
      exit_scls = exit_dzr.entries_by_type("SCLS")[zone_exit.scls_exit_index]
      exit_scls.dest_stage_name = zone_entrance.stage_name
      exit_scls.room_index = zone_entrance.room_num
      exit_scls.spawn_id = zone_entrance.spawn_id
      exit_scls.save_changes()

      # Also update the extra exits when leaving Savage Labyrinth to put you on the correct entrance when leaving.
      if zone_exit.unique_name == "Savage Labyrinth":
        for stage_and_room_name in ["Cave10/Room0", "Cave10/Room20", "Cave11/Room0"]:
          savage_dzr_path = "files/res/Stage/%s.arc" % stage_and_room_name
          savage_dzr = self.get_arc(savage_dzr_path).get_file("room.dzr")
          exit_sclses = [x for x in savage_dzr.entries_by_type("SCLS") if x.dest_stage_name == "sea"]
          for exit_scls in exit_sclses:
            exit_scls.dest_stage_name = zone_entrance.stage_name
            exit_scls.room_index = zone_entrance.room_num
            exit_scls.spawn_id = zone_entrance.spawn_id
            exit_scls.save_changes()

      if zone_exit in CAVE_EXITS:
        # Update the sector coordinates in the 2DMA chunk so that save-and-quitting in a secret cave puts you on the correct island.
        exit_dzs_path = "files/res/Stage/%s/Stage.arc" % zone_exit.stage_name
        exit_dzs = self.get_arc(exit_dzs_path).get_file("stage.dzs")
        _2dma = exit_dzs.entries_by_type("2DMA")[0]
        island_number = self.island_name_to_number[zone_entrance.island_name]
        sector_x = (island_number-1) % 7
        sector_y = (island_number-1) // 7
        _2dma.sector_x = sector_x-3
        _2dma.sector_y = sector_y-3
        _2dma.save_changes()

      if zone_exit.unique_name == "Fire Mountain Secret Cave" and zone_entrance.entrance_name != "Crater on Fire Mountain":
        actors = exit_dzr.entries_by_type("ACTR")
        for actor in actors:
          if actor.name == "VolTag":
            kill_trigger = actor
            break
        if zone_entrance.entrance_name == "Palsa on Ice Ring Isle":
          # Ice Ring's entrance leads to Fire Mountain's exit.
          # Change the kill trigger on the inside of Fire Mountain to act like the one inside Ice Ring.
          kill_trigger.type = 2
          kill_trigger.save_changes()
        else:
          # An entrance without a timer leads into this cave.
          # Remove the kill trigger actor on the inside, because otherwise it would throw the player out the instant they enter.
          exit_dzr.remove_entity(kill_trigger, "ACTR")

      if zone_exit.unique_name == "Ice Ring Isle Secret Cave":
        # Also update the inner cave of Ice Ring Isle to take you out to the correct entrance as well.
        inner_cave_dzr_path = "files/res/Stage/ITest62/Room0.arc"
        inner_cave_dzr = self.get_arc(inner_cave_dzr_path).get_file("room.dzr")
        inner_cave_exit_scls = inner_cave_dzr.entries_by_type("SCLS")[0]
        inner_cave_exit_scls.dest_stage_name = zone_entrance.stage_name
        inner_cave_exit_scls.room_index = zone_entrance.room_num
        inner_cave_exit_scls.spawn_id = zone_entrance.spawn_id
        inner_cave_exit_scls.save_changes()

        # Also update the sector coordinates in the 2DMA chunk of the inner cave of Ice Ring Isle so save-and-quitting works properly there.
        inner_cave_dzs_path = "files/res/Stage/ITest62/Stage.arc"
        inner_cave_dzs = self.get_arc(inner_cave_dzs_path).get_file("stage.dzs")
        inner_cave_2dma = inner_cave_dzs.entries_by_type("2DMA")[0]
        inner_cave_2dma.sector_x = sector_x-3
        inner_cave_2dma.sector_y = sector_y-3
        inner_cave_2dma.save_changes()

        actors = exit_dzr.entries_by_type("ACTR")
        for actor in actors:
          if actor.name == "VolTag":
            kill_trigger = actor
            break
        if zone_entrance.entrance_name == "Palsa on Ice Ring Isle":
          # Unchanged from vanilla, do nothing.
          pass
        elif zone_entrance.entrance_name == "Crater on Fire Mountain":
          # Fire Mountain's entrance leads to Ice Ring's exit.
          # Change the kill trigger on the inside of Ice Ring to act like the one inside Fire Mountain.
          kill_trigger.type = 1
          kill_trigger.save_changes()
        else:
          # An entrance without a timer leads into this cave.
          # Remove the kill trigger actor on the inside, because otherwise it would throw the player out the instant they enter.
          exit_dzr.remove_entity(kill_trigger, "ACTR")


      if zone_exit.boss_stage_name is not None:
        # Update the wind warp out event to take you to the correct island.
        boss_stage_arc_path = "files/res/Stage/%s/Stage.arc" % zone_exit.boss_stage_name
        event_list = self.get_arc(boss_stage_arc_path).get_file("event_list.dat")
        warp_out_event = event_list.events_by_name["WARP_WIND_AFTER"]
        for actor in warp_out_event.actors:
          if actor.name == "DIRECTOR":
            director = actor
            break
        for action in director.actions:
          if action.name == "NEXT":
            stage_change_action = action
            break
        stgNProp = False
        romNProp = False
        spnIProp = False
        for prop in stage_change_action.properties:
          if prop.name == "Stage" and not stgNProp:
            stage_name_prop = prop
            stgNProp = True
            continue
          elif prop.name == "RoomNo" and not romNProp:
            room_num_prop = prop
            romNProp = True
            continue
          elif prop.name == "StartCode" and not spnIProp:
            spawn_id_prop = prop
            spnIProp = True
            continue
        stage_name_prop.value = zone_entrance.warp_out_stage_name
        room_num_prop.value = zone_entrance.warp_out_room_num
        spawn_id_prop.value = zone_entrance.warp_out_spawn_id

  self.logic.update_entrance_connection_macros()
