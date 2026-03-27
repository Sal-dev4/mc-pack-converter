from __future__ import annotations

LEGACY_ITEM_FILE_RENAMES = {
    # tools
    "gold_sword.png": "golden_sword.png",
    "wood_sword.png": "wooden_sword.png",
    "gold_pickaxe.png": "golden_pickaxe.png",
    "wood_pickaxe.png": "wooden_pickaxe.png",
    "gold_axe.png": "golden_axe.png",
    "wood_axe.png": "wooden_axe.png",
    "gold_shovel.png": "golden_shovel.png",
    "wood_shovel.png": "wooden_shovel.png",
    "gold_hoe.png": "golden_hoe.png",
    "wood_hoe.png": "wooden_hoe.png",

    # armor
    "gold_helmet.png": "golden_helmet.png",
    "gold_chestplate.png": "golden_chestplate.png",
    "gold_leggings.png": "golden_leggings.png",
    "gold_boots.png": "golden_boots.png",
    "gold_horse_armor.png": "golden_horse_armor.png",

    # foods / utility
    "apple_golden.png": "golden_apple.png",
    "carrot_golden.png": "golden_carrot.png",
    "melon_speckled.png": "glistering_melon_slice.png",
    "book_enchanted.png": "enchanted_book.png",
    "door_wood.png": "oak_door.png",
    "boat.png": "oak_boat.png",
    "reeds.png": "sugar_cane.png",
    "redstone_dust.png": "redstone.png",
    "netherbrick.png": "nether_brick.png",
    "brick.png": "brick.png",

    # fireworks
    "fireworks.png": "firework_rocket.png",
    "fireworks_charge.png": "firework_star.png",

    # fish
    "fish_cod_raw.png": "cod.png",
    "fish_cod_cooked.png": "cooked_cod.png",
    "fish_salmon_raw.png": "salmon.png",
    "fish_salmon_cooked.png": "cooked_salmon.png",
    "fish_clownfish_raw.png": "tropical_fish.png",
    "fish_pufferfish_raw.png": "pufferfish.png",

    # seeds
    "seeds_wheat.png": "wheat_seeds.png",
    "seeds_melon.png": "melon_seeds.png",
    "seeds_pumpkin.png": "pumpkin_seeds.png",

    # dyes
    "dye_powder_black.png": "black_dye.png",
    "dye_powder_blue.png": "blue_dye.png",
    "dye_powder_brown.png": "brown_dye.png",
    "dye_powder_cyan.png": "cyan_dye.png",
    "dye_powder_gray.png": "gray_dye.png",
    "dye_powder_green.png": "green_dye.png",
    "dye_powder_light_blue.png": "light_blue_dye.png",
    "dye_powder_lime.png": "lime_dye.png",
    "dye_powder_magenta.png": "magenta_dye.png",
    "dye_powder_orange.png": "orange_dye.png",
    "dye_powder_pink.png": "pink_dye.png",
    "dye_powder_purple.png": "purple_dye.png",
    "dye_powder_red.png": "red_dye.png",
    "dye_powder_silver.png": "light_gray_dye.png",
    "dye_powder_white.png": "white_dye.png",
    "dye_powder_yellow.png": "yellow_dye.png",

    # music discs
    "record_11.png": "music_disc_11.png",
    "record_13.png": "music_disc_13.png",
    "record_blocks.png": "music_disc_blocks.png",
    "record_cat.png": "music_disc_cat.png",
    "record_chirp.png": "music_disc_chirp.png",
    "record_far.png": "music_disc_far.png",
    "record_mall.png": "music_disc_mall.png",
    "record_mellohi.png": "music_disc_mellohi.png",
    "record_stal.png": "music_disc_stal.png",
    "record_strad.png": "music_disc_strad.png",
    "record_wait.png": "music_disc_wait.png",
    "record_ward.png": "music_disc_ward.png",

    # minecarts
    "minecart_chest.png": "chest_minecart.png",
    "minecart_command_block.png": "command_block_minecart.png",
    "minecart_furnace.png": "furnace_minecart.png",
    "minecart_hopper.png": "hopper_minecart.png",
    "minecart_tnt.png": "tnt_minecart.png",

    # rails/items misc
    "cauldron.png": "cauldron.png",
    "comparator.png": "comparator.png",
    "comparator_on.png": "comparator.png",
    "repeater.png": "repeater.png",
    "repeater_on.png": "repeater.png",

    # renamed simple items
    "banner.png": "white_banner.png",
    "bed.png": "red_bed.png",
    "chorus_fruit_popped.png": "popped_chorus_fruit.png",
    "clownfish.png": "tropical_fish.png",
    "cookie.png": "cookie.png",
    "gunpowder.png": "gunpowder.png",
    "magma_cream.png": "magma_cream.png",
    "map_empty.png": "map.png",
    "map_filled.png": "filled_map.png",
    "paper.png": "paper.png",
    "porkchop_raw.png": "porkchop.png",
    "porkchop_cooked.png": "cooked_porkchop.png",
    "rabbit_cooked.png": "cooked_rabbit.png",
    "rabbit_raw.png": "rabbit.png",
    "beef_raw.png": "beef.png",
    "beef_cooked.png": "cooked_beef.png",
    "chicken_raw.png": "chicken.png",
    "chicken_cooked.png": "cooked_chicken.png",
    "mutton_raw.png": "mutton.png",
    "mutton_cooked.png": "cooked_mutton.png",
    "sign.png": "oak_sign.png",
    "door_spruce.png": "spruce_door.png",
    "door_birch.png": "birch_door.png",
    "door_jungle.png": "jungle_door.png",
    "door_acacia.png": "acacia_door.png",
    "door_dark_oak.png": "dark_oak_door.png",
    "boat_spruce.png": "spruce_boat.png",
    "boat_birch.png": "birch_boat.png",
    "boat_jungle.png": "jungle_boat.png",
    "boat_acacia.png": "acacia_boat.png",
    "boat_dark_oak.png": "dark_oak_boat.png",

    # special texture-driven items
    "bow_standby.png": "bow.png",
    "fishing_rod_uncast.png": "fishing_rod.png",
    "carrot_on_a_stick.png": "carrot_on_a_stick.png",
    "lead.png": "lead.png",
    "name_tag.png": "name_tag.png",

    # skulls / heads
    "skull_skeleton.png": "skeleton_skull.png",
    "skull_wither.png": "wither_skeleton_skull.png",
    "skull_zombie.png": "zombie_head.png",
    "skull_char.png": "player_head.png",
    "skull_creeper.png": "creeper_head.png",
    "skull_dragon.png": "dragon_head.png",

    # buckets / potion bottles
    "bucket_water.png": "water_bucket.png",
    "bucket_lava.png": "lava_bucket.png",
    "bucket_milk.png": "milk_bucket.png",
    "potion_bottle_drinkable.png": "potion.png",
    "potion_bottle_splash.png": "splash_potion.png",

    # rabbit extras
    "rabbit_foot.png": "rabbit_foot.png",
    "rabbit_hide.png": "rabbit_hide.png",
    "rabbit_stew.png": "rabbit_stew.png",

    # doors / misc old forms
    "door_iron.png": "iron_door.png",
    "speckled_melon.png": "glistering_melon_slice.png",

    # a few common later-name items
    "totem.png": "totem_of_undying.png",
    "totem_undying.png": "totem_of_undying.png",

        # skulls / heads
    "skull_skeleton.png": "skeleton_skull.png",
    "skull_wither.png": "wither_skeleton_skull.png",
    "skull_zombie.png": "zombie_head.png",
    "skull_char.png": "player_head.png",
    "skull_creeper.png": "creeper_head.png",
    "skull_dragon.png": "dragon_head.png",

    # buckets / potions
    "bucket_water.png": "water_bucket.png",
    "bucket_lava.png": "lava_bucket.png",
    "bucket_milk.png": "milk_bucket.png",
    "potion_bottle_drinkable.png": "potion.png",
    "potion_bottle_splash.png": "splash_potion.png",

    # extra food / drops
    "rabbit_foot.png": "rabbit_foot.png",
    "rabbit_hide.png": "rabbit_hide.png",
    "rabbit_stew.png": "rabbit_stew.png",
    "door_iron.png": "iron_door.png",
    "speckled_melon.png": "glistering_melon_slice.png",

    # later names
    "totem.png": "totem_of_undying.png",
    "totem_undying.png": "totem_of_undying.png",
}

LEGACY_BLOCK_FILE_RENAMES = {
    # grass / dirt / farm
    "grass_side.png": "grass_block_side.png",
    "grass_side_overlay.png": "grass_block_side_overlay.png",
    "grass_top.png": "grass_block_top.png",
    "grass.png": "short_grass.png",
    "farmland_dry.png": "farmland.png",
    "farmland_wet.png": "farmland_moist.png",
    "dirt.png": "dirt.png",
    "coarse_dirt.png": "coarse_dirt.png",
    "podzol_side.png": "podzol_side.png",
    "podzol_top.png": "podzol_top.png",

    # stone variants
    "stone.png": "stone.png",
    "stone_andesite.png": "andesite.png",
    "stone_andesite_smooth.png": "polished_andesite.png",
    "stone_diorite.png": "diorite.png",
    "stone_diorite_smooth.png": "polished_diorite.png",
    "stone_granite.png": "granite.png",
    "stone_granite_smooth.png": "polished_granite.png",

    # stone bricks
    "stonebrick.png": "stone_bricks.png",
    "stonebrick_carved.png": "chiseled_stone_bricks.png",
    "stonebrick_cracked.png": "cracked_stone_bricks.png",
    "stonebrick_mossy.png": "mossy_stone_bricks.png",

    # sandstone
    "sandstone_normal.png": "sandstone.png",
    "sandstone_carved.png": "chiseled_sandstone.png",
    "sandstone_smooth.png": "cut_sandstone.png",
    "sandstone_top.png": "sandstone_top.png",
    "sandstone_bottom.png": "sandstone_bottom.png",

    # red sandstone
    "red_sandstone_normal.png": "red_sandstone.png",
    "red_sandstone_carved.png": "chiseled_red_sandstone.png",
    "red_sandstone_smooth.png": "cut_red_sandstone.png",
    "red_sandstone_top.png": "red_sandstone_top.png",
    "red_sandstone_bottom.png": "red_sandstone_bottom.png",

    # quartz
    "quartz_block_chiseled.png": "chiseled_quartz_block.png",
    "quartz_block_chiseled_top.png": "chiseled_quartz_block_top.png",
    "quartz_block_lines.png": "quartz_pillar.png",
    "quartz_block_lines_top.png": "quartz_pillar_top.png",
    "quartz_block_side.png": "quartz_block_side.png",
    "quartz_block_top.png": "quartz_block_top.png",
    "quartz_block_bottom.png": "quartz_block_bottom.png",
    "quartz_ore.png": "nether_quartz_ore.png",

    # bricks
    "brick.png": "bricks.png",
    "nether_brick.png": "nether_bricks.png",
    "red_nether_brick.png": "red_nether_bricks.png",
    "end_bricks.png": "end_stone_bricks.png",

    # purpur
    "purpur_block.png": "purpur_block.png",
    "purpur_pillar.png": "purpur_pillar.png",
    "purpur_pillar_top.png": "purpur_pillar_top.png",

    # basic blocks
    "obsidian.png": "obsidian.png",
    "bedrock.png": "bedrock.png",
    "netherrack.png": "netherrack.png",
    "soulsand.png": "soul_sand.png",
    "magma.png": "magma_block.png",
    "ice.png": "ice.png",
    "ice_packed.png": "packed_ice.png",
    "snow.png": "snow.png",
    "clay.png": "clay.png",
    "gravel.png": "gravel.png",
    "sand.png": "sand.png",
    "red_sand.png": "red_sand.png",
    "sponge.png": "sponge.png",
    "sponge_wet.png": "wet_sponge.png",
    "slime.png": "slime_block.png",
    "hay_block_side.png": "hay_block_side.png",
    "hay_block_top.png": "hay_block_top.png",
    "portal.png": "nether_portal.png",

    # ores
    "coal_ore.png": "coal_ore.png",
    "iron_ore.png": "iron_ore.png",
    "gold_ore.png": "gold_ore.png",
    "diamond_ore.png": "diamond_ore.png",
    "emerald_ore.png": "emerald_ore.png",
    "lapis_ore.png": "lapis_ore.png",
    "redstone_ore.png": "redstone_ore.png",
    "redstone_ore_lit.png": "redstone_ore.png",

    # ore blocks
    "coal_block.png": "coal_block.png",
    "iron_block.png": "iron_block.png",
    "gold_block.png": "gold_block.png",
    "diamond_block.png": "diamond_block.png",
    "emerald_block.png": "emerald_block.png",
    "lapis_block.png": "lapis_block.png",
    "redstone_block.png": "redstone_block.png",

    # logs
    "log_oak.png": "oak_log.png",
    "log_oak_top.png": "oak_log_top.png",
    "log_spruce.png": "spruce_log.png",
    "log_spruce_top.png": "spruce_log_top.png",
    "log_birch.png": "birch_log.png",
    "log_birch_top.png": "birch_log_top.png",
    "log_jungle.png": "jungle_log.png",
    "log_jungle_top.png": "jungle_log_top.png",
    "log_big_oak.png": "dark_oak_log.png",
    "log_big_oak_top.png": "dark_oak_log_top.png",
    "log_acacia.png": "acacia_log.png",
    "log_acacia_top.png": "acacia_log_top.png",

    # planks
    "planks_oak.png": "oak_planks.png",
    "planks_spruce.png": "spruce_planks.png",
    "planks_birch.png": "birch_planks.png",
    "planks_jungle.png": "jungle_planks.png",
    "planks_big_oak.png": "dark_oak_planks.png",
    "planks_acacia.png": "acacia_planks.png",

    # leaves
    "leaves_oak.png": "oak_leaves.png",
    "leaves_spruce.png": "spruce_leaves.png",
    "leaves_birch.png": "birch_leaves.png",
    "leaves_jungle.png": "jungle_leaves.png",
    "leaves_big_oak.png": "dark_oak_leaves.png",
    "leaves_acacia.png": "acacia_leaves.png",

    # saplings
    "sapling_oak.png": "oak_sapling.png",
    "sapling_spruce.png": "spruce_sapling.png",
    "sapling_birch.png": "birch_sapling.png",
    "sapling_jungle.png": "jungle_sapling.png",
    "sapling_roofed_oak.png": "dark_oak_sapling.png",
    "sapling_acacia.png": "acacia_sapling.png",

    # doors
    "door_wood_lower.png": "oak_door_bottom.png",
    "door_wood_upper.png": "oak_door_top.png",
    "door_iron_lower.png": "iron_door_bottom.png",
    "door_iron_upper.png": "iron_door_top.png",
    "door_spruce_lower.png": "spruce_door_bottom.png",
    "door_spruce_upper.png": "spruce_door_top.png",
    "door_birch_lower.png": "birch_door_bottom.png",
    "door_birch_upper.png": "birch_door_top.png",
    "door_jungle_lower.png": "jungle_door_bottom.png",
    "door_jungle_upper.png": "jungle_door_top.png",
    "door_acacia_lower.png": "acacia_door_bottom.png",
    "door_acacia_upper.png": "acacia_door_top.png",
    "door_dark_oak_lower.png": "dark_oak_door_bottom.png",
    "door_dark_oak_upper.png": "dark_oak_door_top.png",

    # rails
    "rail_normal.png": "rail.png",
    "rail_normal_turned.png": "rail_corner.png",
    "rail_golden.png": "powered_rail.png",
    "rail_golden_powered.png": "powered_rail_on.png",
    "rail_detector.png": "detector_rail.png",
    "rail_detector_powered.png": "detector_rail_on.png",
    "rail_activator.png": "activator_rail.png",
    "rail_activator_powered.png": "activator_rail_on.png",

    # redstone / machines
    "redstone_lamp_off.png": "redstone_lamp.png",
    "redstone_lamp_on.png": "redstone_lamp_on.png",
    "noteblock.png": "note_block.png",
    "bookshelf.png": "bookshelf.png",
    "crafting_table_front.png": "crafting_table_front.png",
    "crafting_table_side.png": "crafting_table_side.png",
    "crafting_table_top.png": "crafting_table_top.png",
    "furnace_front_off.png": "furnace_front.png",
    "furnace_front_on.png": "furnace_front_on.png",
    "furnace_side.png": "furnace_side.png",
    "furnace_top.png": "furnace_top.png",
    "dispenser_front_horizontal.png": "dispenser_front.png",
    "dispenser_front_vertical.png": "dispenser_front_vertical.png",
    "dropper_front_horizontal.png": "dropper_front.png",
    "dropper_front_vertical.png": "dropper_front_vertical.png",
    "command_block.png": "command_block_front.png",
    "command_block_back.png": "command_block_back.png",
    "command_block_conditional.png": "command_block_conditional.png",
    "command_block_side.png": "command_block_side.png",
    "beacon.png": "beacon.png",
    "daylight_detector_side.png": "daylight_detector_side.png",
    "daylight_detector_top.png": "daylight_detector_top.png",
    "hopper_inside.png": "hopper_inside.png",
    "hopper_outside.png": "hopper_outside.png",
    "hopper_top.png": "hopper_top.png",

    # pistons
    "piston_bottom.png": "piston_bottom.png",
    "piston_inner.png": "piston_inner.png",
    "piston_side.png": "piston_side.png",
    "piston_top_normal.png": "piston_top.png",
    "piston_top_sticky.png": "sticky_piston_top.png",

    # crops
    "wheat_stage_0.png": "wheat_stage0.png",
    "wheat_stage_1.png": "wheat_stage1.png",
    "wheat_stage_2.png": "wheat_stage2.png",
    "wheat_stage_3.png": "wheat_stage3.png",
    "wheat_stage_4.png": "wheat_stage4.png",
    "wheat_stage_5.png": "wheat_stage5.png",
    "wheat_stage_6.png": "wheat_stage6.png",
    "wheat_stage_7.png": "wheat_stage7.png",
    "carrots_stage_0.png": "carrots_stage0.png",
    "carrots_stage_1.png": "carrots_stage1.png",
    "carrots_stage_2.png": "carrots_stage2.png",
    "carrots_stage_3.png": "carrots_stage3.png",
    "potatoes_stage_0.png": "potatoes_stage0.png",
    "potatoes_stage_1.png": "potatoes_stage1.png",
    "potatoes_stage_2.png": "potatoes_stage2.png",
    "potatoes_stage_3.png": "potatoes_stage3.png",
    "nether_wart_stage_0.png": "nether_wart_stage0.png",
    "nether_wart_stage_1.png": "nether_wart_stage1.png",
    "nether_wart_stage_2.png": "nether_wart_stage2.png",

    # melon / pumpkin
    "melon_side.png": "melon_side.png",
    "melon_top.png": "melon_top.png",
    "pumpkin_face_off.png": "pumpkin_face.png",
    "pumpkin_face_on.png": "jack_o_lantern.png",
    "pumpkin_side.png": "pumpkin_side.png",
    "pumpkin_top.png": "pumpkin_top.png",

    # cactus / plant / misc
    "cactus_bottom.png": "cactus_bottom.png",
    "cactus_side.png": "cactus_side.png",
    "cactus_top.png": "cactus_top.png",
    "ladder.png": "ladder.png",
    "vine.png": "vine.png",
    "web.png": "cobweb.png",
    "waterlily.png": "lily_pad.png",
    "reeds.png": "sugar_cane.png",

    # mushroom blocks
    "mushroom_block_skin_brown.png": "brown_mushroom_block.png",
    "mushroom_block_skin_red.png": "red_mushroom_block.png",
    "mushroom_block_skin_stem.png": "mushroom_stem.png",
    "mushroom_block_inside.png": "mushroom_block_inside.png",

    # chests
    "chest_front.png": "chest_front.png",
    "chest_side.png": "chest_side.png",
    "chest_top.png": "chest_top.png",
    "ender_chest.png": "ender_chest.png",
    "ender_chest_top.png": "ender_chest_top.png",
    "trapped_chest_front.png": "trapped_chest_front.png",
    "trapped_chest_side.png": "trapped_chest_side.png",
    "trapped_chest_top.png": "trapped_chest_top.png",

    # TNT
    "tnt_bottom.png": "tnt_bottom.png",
    "tnt_side.png": "tnt_side.png",
    "tnt_top.png": "tnt_top.png",

    # prismarine
    "prismarine_rough.png": "prismarine.png",
    "prismarine_bricks.png": "prismarine_bricks.png",
    "prismarine_dark.png": "dark_prismarine.png",

    # anvil
    "anvil_base.png": "anvil.png",
    "anvil_top_damaged_0.png": "anvil_top.png",
    "anvil_top_damaged_1.png": "chipped_anvil_top.png",
    "anvil_top_damaged_2.png": "damaged_anvil_top.png",

    # wool
    "wool_colored_white.png": "white_wool.png",
    "wool_colored_orange.png": "orange_wool.png",
    "wool_colored_magenta.png": "magenta_wool.png",
    "wool_colored_light_blue.png": "light_blue_wool.png",
    "wool_colored_yellow.png": "yellow_wool.png",
    "wool_colored_lime.png": "lime_wool.png",
    "wool_colored_pink.png": "pink_wool.png",
    "wool_colored_gray.png": "gray_wool.png",
    "wool_colored_silver.png": "light_gray_wool.png",
    "wool_colored_cyan.png": "cyan_wool.png",
    "wool_colored_purple.png": "purple_wool.png",
    "wool_colored_blue.png": "blue_wool.png",
    "wool_colored_brown.png": "brown_wool.png",
    "wool_colored_green.png": "green_wool.png",
    "wool_colored_red.png": "red_wool.png",
    "wool_colored_black.png": "black_wool.png",

    # carpet
    "carpet_white.png": "white_carpet.png",
    "carpet_orange.png": "orange_carpet.png",
    "carpet_magenta.png": "magenta_carpet.png",
    "carpet_light_blue.png": "light_blue_carpet.png",
    "carpet_yellow.png": "yellow_carpet.png",
    "carpet_lime.png": "lime_carpet.png",
    "carpet_pink.png": "pink_carpet.png",
    "carpet_gray.png": "gray_carpet.png",
    "carpet_silver.png": "light_gray_carpet.png",
    "carpet_cyan.png": "cyan_carpet.png",
    "carpet_purple.png": "purple_carpet.png",
    "carpet_blue.png": "blue_carpet.png",
    "carpet_brown.png": "brown_carpet.png",
    "carpet_green.png": "green_carpet.png",
    "carpet_red.png": "red_carpet.png",
    "carpet_black.png": "black_carpet.png",

    # terracotta
    "hardened_clay.png": "terracotta.png",
    "hardened_clay_stained_white.png": "white_terracotta.png",
    "hardened_clay_stained_orange.png": "orange_terracotta.png",
    "hardened_clay_stained_magenta.png": "magenta_terracotta.png",
    "hardened_clay_stained_light_blue.png": "light_blue_terracotta.png",
    "hardened_clay_stained_yellow.png": "yellow_terracotta.png",
    "hardened_clay_stained_lime.png": "lime_terracotta.png",
    "hardened_clay_stained_pink.png": "pink_terracotta.png",
    "hardened_clay_stained_gray.png": "gray_terracotta.png",
    "hardened_clay_stained_silver.png": "light_gray_terracotta.png",
    "hardened_clay_stained_cyan.png": "cyan_terracotta.png",
    "hardened_clay_stained_purple.png": "purple_terracotta.png",
    "hardened_clay_stained_blue.png": "blue_terracotta.png",
    "hardened_clay_stained_brown.png": "brown_terracotta.png",
    "hardened_clay_stained_green.png": "green_terracotta.png",
    "hardened_clay_stained_red.png": "red_terracotta.png",
    "hardened_clay_stained_black.png": "black_terracotta.png",

    # stained glass
    "glass_white.png": "white_stained_glass.png",
    "glass_orange.png": "orange_stained_glass.png",
    "glass_magenta.png": "magenta_stained_glass.png",
    "glass_light_blue.png": "light_blue_stained_glass.png",
    "glass_yellow.png": "yellow_stained_glass.png",
    "glass_lime.png": "lime_stained_glass.png",
    "glass_pink.png": "pink_stained_glass.png",
    "glass_gray.png": "gray_stained_glass.png",
    "glass_silver.png": "light_gray_stained_glass.png",
    "glass_cyan.png": "cyan_stained_glass.png",
    "glass_purple.png": "purple_stained_glass.png",
    "glass_blue.png": "blue_stained_glass.png",
    "glass_brown.png": "brown_stained_glass.png",
    "glass_green.png": "green_stained_glass.png",
    "glass_red.png": "red_stained_glass.png",
    "glass_black.png": "black_stained_glass.png",

    # stained glass pane tops
    "glass_pane_top_white.png": "white_stained_glass_pane_top.png",
    "glass_pane_top_orange.png": "orange_stained_glass_pane_top.png",
    "glass_pane_top_magenta.png": "magenta_stained_glass_pane_top.png",
    "glass_pane_top_light_blue.png": "light_blue_stained_glass_pane_top.png",
    "glass_pane_top_yellow.png": "yellow_stained_glass_pane_top.png",
    "glass_pane_top_lime.png": "lime_stained_glass_pane_top.png",
    "glass_pane_top_pink.png": "pink_stained_glass_pane_top.png",
    "glass_pane_top_gray.png": "gray_stained_glass_pane_top.png",
    "glass_pane_top_silver.png": "light_gray_stained_glass_pane_top.png",
    "glass_pane_top_cyan.png": "cyan_stained_glass_pane_top.png",
    "glass_pane_top_purple.png": "purple_stained_glass_pane_top.png",
    "glass_pane_top_blue.png": "blue_stained_glass_pane_top.png",
    "glass_pane_top_brown.png": "brown_stained_glass_pane_top.png",
    "glass_pane_top_green.png": "green_stained_glass_pane_top.png",
    "glass_pane_top_red.png": "red_stained_glass_pane_top.png",
    "glass_pane_top_black.png": "black_stained_glass_pane_top.png",

    # bricks / nether bricks / end stone bricks
    "brick.png": "bricks.png",
    "nether_brick.png": "nether_bricks.png",
    "red_nether_brick.png": "red_nether_bricks.png",
    "end_bricks.png": "end_stone_bricks.png",

    # mushroom blocks
    "mushroom_block_skin_brown.png": "brown_mushroom_block.png",
    "mushroom_block_skin_red.png": "red_mushroom_block.png",
    "mushroom_block_skin_stem.png": "mushroom_stem.png",
    "mushroom_block_inside.png": "mushroom_block_inside.png",

    # sandstone / red sandstone tops and bottoms
    "sandstone_top.png": "sandstone_top.png",
    "sandstone_bottom.png": "sandstone_bottom.png",
    "red_sandstone_top.png": "red_sandstone_top.png",
    "red_sandstone_bottom.png": "red_sandstone_bottom.png",

    # quartz
    "quartz_block_chiseled.png": "chiseled_quartz_block.png",
    "quartz_block_chiseled_top.png": "chiseled_quartz_block_top.png",
    "quartz_block_lines.png": "quartz_pillar.png",
    "quartz_block_lines_top.png": "quartz_pillar_top.png",
    "quartz_block_side.png": "quartz_block_side.png",
    "quartz_block_top.png": "quartz_block_top.png",
    "quartz_ore.png": "nether_quartz_ore.png",

    # purpur
    "purpur_block.png": "purpur_block.png",
    "purpur_pillar.png": "purpur_pillar.png",
    "purpur_pillar_top.png": "purpur_pillar_top.png",

    # obsidian / bedrock / netherrack / soul sand / magma
    "obsidian.png": "obsidian.png",
    "bedrock.png": "bedrock.png",
    "netherrack.png": "netherrack.png",
    "soulsand.png": "soul_sand.png",
    "magma.png": "magma_block.png",

    # ice / packed ice / snow
    "ice.png": "ice.png",
    "ice_packed.png": "packed_ice.png",
    "snow.png": "snow.png",

    # clay / gravel / sand
    "clay.png": "clay.png",
    "gravel.png": "gravel.png",
    "sand.png": "sand.png",
    "red_sand.png": "red_sand.png",

    # stone variants
    "stone.png": "stone.png",
    "stone_andesite.png": "andesite.png",
    "stone_andesite_smooth.png": "polished_andesite.png",
    "stone_diorite.png": "diorite.png",
    "stone_diorite_smooth.png": "polished_diorite.png",
    "stone_granite.png": "granite.png",
    "stone_granite_smooth.png": "polished_granite.png",

    # ores
    "coal_ore.png": "coal_ore.png",
    "iron_ore.png": "iron_ore.png",
    "gold_ore.png": "gold_ore.png",
    "diamond_ore.png": "diamond_ore.png",
    "emerald_ore.png": "emerald_ore.png",
    "lapis_ore.png": "lapis_ore.png",
    "redstone_ore.png": "redstone_ore.png",
    "redstone_ore_lit.png": "redstone_ore.png",
    "quartz_ore.png": "nether_quartz_ore.png",

    # ore blocks / storage blocks
    "coal_block.png": "coal_block.png",
    "iron_block.png": "iron_block.png",
    "gold_block.png": "gold_block.png",
    "diamond_block.png": "diamond_block.png",
    "emerald_block.png": "emerald_block.png",
    "lapis_block.png": "lapis_block.png",
    "redstone_block.png": "redstone_block.png",
    "quartz_block_bottom.png": "quartz_block_bottom.png",

    # bookshelves / crafting / furnace / dispenser / dropper
    "bookshelf.png": "bookshelf.png",
    "crafting_table_front.png": "crafting_table_front.png",
    "crafting_table_side.png": "crafting_table_side.png",
    "crafting_table_top.png": "crafting_table_top.png",
    "furnace_front_off.png": "furnace_front.png",
    "furnace_front_on.png": "furnace_front_on.png",
    "furnace_side.png": "furnace_side.png",
    "furnace_top.png": "furnace_top.png",
    "dispenser_front_horizontal.png": "dispenser_front.png",
    "dispenser_front_vertical.png": "dispenser_front_vertical.png",
    "dropper_front_horizontal.png": "dropper_front.png",
    "dropper_front_vertical.png": "dropper_front_vertical.png",

    # note block / jukebox / enchanting / command block
    "noteblock.png": "note_block.png",
    "jukebox_side.png": "jukebox_side.png",
    "jukebox_top.png": "jukebox_top.png",
    "enchanting_table_bottom.png": "enchanting_table_bottom.png",
    "enchanting_table_side.png": "enchanting_table_side.png",
    "enchanting_table_top.png": "enchanting_table_top.png",
    "command_block.png": "command_block_front.png",
    "command_block_back.png": "command_block_back.png",
    "command_block_conditional.png": "command_block_conditional.png",
    "command_block_side.png": "command_block_side.png",

    # pistons
    "piston_bottom.png": "piston_bottom.png",
    "piston_inner.png": "piston_inner.png",
    "piston_side.png": "piston_side.png",
    "piston_top_normal.png": "piston_top.png",
    "piston_top_sticky.png": "sticky_piston_top.png",

    # cactus / reeds / crops
    "cactus_bottom.png": "cactus_bottom.png",
    "cactus_side.png": "cactus_side.png",
    "cactus_top.png": "cactus_top.png",
    "reeds.png": "sugar_cane.png",
    "wheat_stage_0.png": "wheat_stage0.png",
    "wheat_stage_1.png": "wheat_stage1.png",
    "wheat_stage_2.png": "wheat_stage2.png",
    "wheat_stage_3.png": "wheat_stage3.png",
    "wheat_stage_4.png": "wheat_stage4.png",
    "wheat_stage_5.png": "wheat_stage5.png",
    "wheat_stage_6.png": "wheat_stage6.png",
    "wheat_stage_7.png": "wheat_stage7.png",
    "carrots_stage_0.png": "carrots_stage0.png",
    "carrots_stage_1.png": "carrots_stage1.png",
    "carrots_stage_2.png": "carrots_stage2.png",
    "carrots_stage_3.png": "carrots_stage3.png",
    "potatoes_stage_0.png": "potatoes_stage0.png",
    "potatoes_stage_1.png": "potatoes_stage1.png",
    "potatoes_stage_2.png": "potatoes_stage2.png",
    "potatoes_stage_3.png": "potatoes_stage3.png",
    "nether_wart_stage_0.png": "nether_wart_stage0.png",
    "nether_wart_stage_1.png": "nether_wart_stage1.png",
    "nether_wart_stage_2.png": "nether_wart_stage2.png",

    # melon / pumpkin
    "melon_side.png": "melon_side.png",
    "melon_top.png": "melon_top.png",
    "pumpkin_face_off.png": "pumpkin_face.png",
    "pumpkin_face_on.png": "jack_o_lantern.png",
    "pumpkin_side.png": "pumpkin_side.png",
    "pumpkin_top.png": "pumpkin_top.png",

    # chest / ender chest / trapped chest
    "chest_front.png": "chest_front.png",
    "chest_side.png": "chest_side.png",
    "chest_top.png": "chest_top.png",
    "ender_chest.png": "ender_chest.png",
    "ender_chest_top.png": "ender_chest_top.png",
    "trapped_chest_front.png": "trapped_chest_front.png",
    "trapped_chest_side.png": "trapped_chest_side.png",
    "trapped_chest_top.png": "trapped_chest_top.png",

    # sponge
    "sponge.png": "sponge.png",
    "sponge_wet.png": "wet_sponge.png",

    # hay / slime
    "hay_block_side.png": "hay_block_side.png",
    "hay_block_top.png": "hay_block_top.png",
    "slime.png": "slime_block.png",

    # anvil
    "anvil_base.png": "anvil.png",
    "anvil_top_damaged_0.png": "anvil_top.png",
    "anvil_top_damaged_1.png": "chipped_anvil_top.png",
    "anvil_top_damaged_2.png": "damaged_anvil_top.png",

    # beacon / daylight detector / hopper
    "beacon.png": "beacon.png",
    "daylight_detector_side.png": "daylight_detector_side.png",
    "daylight_detector_top.png": "daylight_detector_top.png",
    "hopper_inside.png": "hopper_inside.png",
    "hopper_outside.png": "hopper_outside.png",
    "hopper_top.png": "hopper_top.png",

    # ladder / vine / cobweb / waterlily
    "ladder.png": "ladder.png",
    "vine.png": "vine.png",
    "web.png": "cobweb.png",
    "waterlily.png": "lily_pad.png",

    # TNT
    "tnt_bottom.png": "tnt_bottom.png",
    "tnt_side.png": "tnt_side.png",
    "tnt_top.png": "tnt_top.png",

        # flowers
    "flower_rose.png": "poppy.png",
    "flower_dandelion.png": "dandelion.png",
    "flower_allium.png": "allium.png",
    "flower_blue_orchid.png": "blue_orchid.png",
    "flower_houstonia.png": "azure_bluet.png",
    "flower_oxeye_daisy.png": "oxeye_daisy.png",
    "flower_tulip_orange.png": "orange_tulip.png",
    "flower_tulip_red.png": "red_tulip.png",
    "flower_tulip_white.png": "white_tulip.png",
    "flower_tulip_pink.png": "pink_tulip.png",

    # double plants
    "double_plant_grass_bottom.png": "tall_grass_bottom.png",
    "double_plant_grass_top.png": "tall_grass_top.png",
    "double_plant_fern_bottom.png": "large_fern_bottom.png",
    "double_plant_fern_top.png": "large_fern_top.png",
    "double_plant_paeonia_bottom.png": "peony_bottom.png",
    "double_plant_paeonia_top.png": "peony_top.png",
    "double_plant_rose_bottom.png": "rose_bush_bottom.png",
    "double_plant_rose_top.png": "rose_bush_top.png",
    "double_plant_sunflower_bottom.png": "sunflower_bottom.png",
    "double_plant_sunflower_back.png": "sunflower_back.png",
    "double_plant_sunflower_front.png": "sunflower_front.png",
    "double_plant_syringa_bottom.png": "lilac_bottom.png",
    "double_plant_syringa_top.png": "lilac_top.png",

    # bushes / plants
    "deadbush.png": "dead_bush.png",

    # mycelium / mossy / end stuff
    "cobblestone_mossy.png": "mossy_cobblestone.png",
    "mycelium_side.png": "mycelium_side.png",
    "mycelium_top.png": "mycelium_top.png",
    "end_stone.png": "end_stone.png",
    "endframe_side.png": "end_portal_frame_side.png",
    "endframe_top.png": "end_portal_frame_top.png",
    "endframe_eye.png": "end_portal_frame_eye.png",

    # brewing / cauldron / spawner
    "brewing_stand.png": "brewing_stand.png",
    "brewing_stand_base.png": "brewing_stand_base.png",
    "cauldron_bottom.png": "cauldron_bottom.png",
    "cauldron_inner.png": "cauldron_inner.png",
    "cauldron_side.png": "cauldron_side.png",
    "cauldron_top.png": "cauldron_top.png",
    "mob_spawner.png": "spawner.png",

    # redstone / torches / tripwire
    "repeater_off.png": "repeater.png",
    "repeater_on.png": "repeater_on.png",
    "comparator_off.png": "comparator.png",
    "comparator_on.png": "comparator_on.png",
    "redstone_torch_on.png": "redstone_torch.png",
    "torch_off.png": "redstone_torch_off.png",
    "torch_on.png": "torch.png",
    "trip_wire.png": "tripwire.png",

    # stems
    "melon_stem_connected.png": "attached_melon_stem.png",
    "melon_stem_disconnected.png": "melon_stem.png",
    "pumpkin_stem_connected.png": "attached_pumpkin_stem.png",
    "pumpkin_stem_disconnected.png": "pumpkin_stem.png",

    # extra blocks
    "dragon_egg.png": "dragon_egg.png",
    "glowstone.png": "glowstone.png",
    "sea_lantern.png": "sea_lantern.png",
    "lever.png": "lever.png",

        # beds
    "bed_feet_end.png": "bed_feet_end.png",
    "bed_feet_side.png": "bed_feet_side.png",
    "bed_feet_top.png": "bed_feet_top.png",
    "bed_head_end.png": "bed_head_end.png",
    "bed_head_side.png": "bed_head_side.png",
    "bed_head_top.png": "bed_head_top.png",

    # cake
    "cake_bottom.png": "cake_bottom.png",
    "cake_inner.png": "cake_inner.png",
    "cake_side.png": "cake_side.png",
    "cake_top.png": "cake_top.png",

    # trapdoors
    "trapdoor.png": "oak_trapdoor.png",
    "trapdoor_spruce.png": "spruce_trapdoor.png",
    "trapdoor_birch.png": "birch_trapdoor.png",
    "trapdoor_jungle.png": "jungle_trapdoor.png",
    "trapdoor_acacia.png": "acacia_trapdoor.png",
    "trapdoor_dark_oak.png": "dark_oak_trapdoor.png",
    "iron_trapdoor.png": "iron_trapdoor.png",

    # fences
    "fence_oak.png": "oak_fence.png",
    "fence_spruce.png": "spruce_fence.png",
    "fence_birch.png": "birch_fence.png",
    "fence_jungle.png": "jungle_fence.png",
    "fence_acacia.png": "acacia_fence.png",
    "fence_big_oak.png": "dark_oak_fence.png",
    "nether_brick_fence.png": "nether_brick_fence.png",

    # fence gates
    "fence_gate_oak.png": "oak_fence_gate.png",
    "fence_gate_spruce.png": "spruce_fence_gate.png",
    "fence_gate_birch.png": "birch_fence_gate.png",
    "fence_gate_jungle.png": "jungle_fence_gate.png",
    "fence_gate_acacia.png": "acacia_fence_gate.png",
    "fence_gate_big_oak.png": "dark_oak_fence_gate.png",

    # slabs
    "wood_slab_top_oak.png": "oak_planks.png",
    "wood_slab_top_spruce.png": "spruce_planks.png",
    "wood_slab_top_birch.png": "birch_planks.png",
    "wood_slab_top_jungle.png": "jungle_planks.png",
    "wood_slab_top_acacia.png": "acacia_planks.png",
    "wood_slab_top_big_oak.png": "dark_oak_planks.png",

    # pressure plates
    "pressure_plate_wood.png": "oak_planks.png",
    "pressure_plate_stone.png": "stone.png",
    "pressure_plate_iron.png": "iron_block.png",
    "pressure_plate_gold.png": "gold_block.png",

    # buttons
    "button_wood.png": "oak_planks.png",
    "button_stone.png": "stone.png",

    # ladders / bars / panes
    "iron_bars.png": "iron_bars.png",
    "glass_pane_top.png": "glass_pane_top.png",

    # cobble / mossy / mossy stone brick related extras
    "cobblestone.png": "cobblestone.png",
    "cobblestone_mossy.png": "mossy_cobblestone.png",

    # bookshelf / table adjacent extras
    "enchanting_table_bottom.png": "enchanting_table_bottom.png",
    "enchanting_table_side.png": "enchanting_table_side.png",
    "enchanting_table_top.png": "enchanting_table_top.png",
    "jukebox_side.png": "jukebox_side.png",
    "jukebox_top.png": "jukebox_top.png",

    # portal / frame / dragon
    "dragon_egg.png": "dragon_egg.png",
    "endframe_side.png": "end_portal_frame_side.png",
    "endframe_top.png": "end_portal_frame_top.png",
    "endframe_eye.png": "end_portal_frame_eye.png",

    # brewing / cauldron / spawner
    "brewing_stand.png": "brewing_stand.png",
    "brewing_stand_base.png": "brewing_stand_base.png",
    "cauldron_bottom.png": "cauldron_bottom.png",
    "cauldron_inner.png": "cauldron_inner.png",
    "cauldron_side.png": "cauldron_side.png",
    "cauldron_top.png": "cauldron_top.png",
    "mob_spawner.png": "spawner.png",

    # redstone wire / dust style block textures
    "redstone_dust_cross.png": "redstone_dust_dot.png",
    "redstone_dust_cross_overlay.png": "redstone_dust_dot.png",
    "redstone_dust_line.png": "redstone_dust_line0.png",
    "redstone_dust_line_overlay.png": "redstone_dust_line0.png",

    # torches / repeaters / comparators
    "repeater_off.png": "repeater.png",
    "repeater_on.png": "repeater_on.png",
    "comparator_off.png": "comparator.png",
    "comparator_on.png": "comparator_on.png",
    "redstone_torch_on.png": "redstone_torch.png",
    "torch_off.png": "redstone_torch_off.png",
    "torch_on.png": "torch.png",

    # stems
    "melon_stem_connected.png": "attached_melon_stem.png",
    "melon_stem_disconnected.png": "melon_stem.png",
    "pumpkin_stem_connected.png": "attached_pumpkin_stem.png",
    "pumpkin_stem_disconnected.png": "pumpkin_stem.png",

    # flowers / plants
    "flower_rose.png": "poppy.png",
    "flower_dandelion.png": "dandelion.png",
    "flower_allium.png": "allium.png",
    "flower_blue_orchid.png": "blue_orchid.png",
    "flower_houstonia.png": "azure_bluet.png",
    "flower_oxeye_daisy.png": "oxeye_daisy.png",
    "flower_tulip_orange.png": "orange_tulip.png",
    "flower_tulip_red.png": "red_tulip.png",
    "flower_tulip_white.png": "white_tulip.png",
    "flower_tulip_pink.png": "pink_tulip.png",
    "deadbush.png": "dead_bush.png",

    # double plants
    "double_plant_grass_bottom.png": "tall_grass_bottom.png",
    "double_plant_grass_top.png": "tall_grass_top.png",
    "double_plant_fern_bottom.png": "large_fern_bottom.png",
    "double_plant_fern_top.png": "large_fern_top.png",
    "double_plant_paeonia_bottom.png": "peony_bottom.png",
    "double_plant_paeonia_top.png": "peony_top.png",
    "double_plant_rose_bottom.png": "rose_bush_bottom.png",
    "double_plant_rose_top.png": "rose_bush_top.png",
    "double_plant_sunflower_bottom.png": "sunflower_bottom.png",
    "double_plant_sunflower_back.png": "sunflower_back.png",
    "double_plant_sunflower_front.png": "sunflower_front.png",
    "double_plant_syringa_bottom.png": "lilac_bottom.png",
    "double_plant_syringa_top.png": "lilac_top.png",
}