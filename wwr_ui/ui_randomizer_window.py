# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomizer_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 973)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vertical_layout_widget = QVBoxLayout(self.centralwidget)
        self.vertical_layout_widget.setObjectName(u"vertical_layout_widget")
        self.scroll_for_main = QScrollArea(self.centralwidget)
        self.scroll_for_main.setObjectName(u"scroll_for_main")
        self.scroll_for_main.setFrameShape(QFrame.NoFrame)
        self.scroll_for_main.setWidgetResizable(True)
        self.content_for_main_scroll = QWidget()
        self.content_for_main_scroll.setObjectName(u"content_for_main_scroll")
        self.content_for_main_scroll.setGeometry(QRect(0, 0, 982, 836))
        self.layout_for_main_scroll = QVBoxLayout(self.content_for_main_scroll)
        self.layout_for_main_scroll.setObjectName(u"layout_for_main_scroll")
        self.layout_for_main_scroll.setContentsMargins(0, 0, 0, 0)
        self.tab_for_main = QTabWidget(self.content_for_main_scroll)
        self.tab_for_main.setObjectName(u"tab_for_main")
        self.tab_for_main.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_for_main.sizePolicy().hasHeightForWidth())
        self.tab_for_main.setSizePolicy(sizePolicy)
        self.tab_for_settings = QWidget()
        self.tab_for_settings.setObjectName(u"tab_for_settings")
        self.layout_for_paths = QVBoxLayout(self.tab_for_settings)
        self.layout_for_paths.setObjectName(u"layout_for_paths")
        self.grid_for_paths = QGridLayout()
        self.grid_for_paths.setObjectName(u"grid_for_paths")
        self.seed = QLineEdit(self.tab_for_settings)
        self.seed.setObjectName(u"seed")

        self.grid_for_paths.addWidget(self.seed, 2, 1, 1, 1)

        self.label_for_clean = QLabel(self.tab_for_settings)
        self.label_for_clean.setObjectName(u"label_for_clean")

        self.grid_for_paths.addWidget(self.label_for_clean, 0, 0, 1, 1)

        self.clean_iso_path = QLineEdit(self.tab_for_settings)
        self.clean_iso_path.setObjectName(u"clean_iso_path")

        self.grid_for_paths.addWidget(self.clean_iso_path, 0, 1, 1, 1)

        self.label_for_output = QLabel(self.tab_for_settings)
        self.label_for_output.setObjectName(u"label_for_output")

        self.grid_for_paths.addWidget(self.label_for_output, 1, 0, 1, 1)

        self.output_folder = QLineEdit(self.tab_for_settings)
        self.output_folder.setObjectName(u"output_folder")

        self.grid_for_paths.addWidget(self.output_folder, 1, 1, 1, 1)

        self.output_folder_browse_button = QPushButton(self.tab_for_settings)
        self.output_folder_browse_button.setObjectName(u"output_folder_browse_button")

        self.grid_for_paths.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)

        self.label_for_seed = QLabel(self.tab_for_settings)
        self.label_for_seed.setObjectName(u"label_for_seed")

        self.grid_for_paths.addWidget(self.label_for_seed, 2, 0, 1, 1)

        self.generate_seed_button = QPushButton(self.tab_for_settings)
        self.generate_seed_button.setObjectName(u"generate_seed_button")

        self.grid_for_paths.addWidget(self.generate_seed_button, 2, 2, 1, 1)

        self.clean_iso_path_browse_button = QPushButton(self.tab_for_settings)
        self.clean_iso_path_browse_button.setObjectName(u"clean_iso_path_browse_button")

        self.grid_for_paths.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)


        self.layout_for_paths.addLayout(self.grid_for_paths)

        self.grid_for_logic = QGridLayout()
        self.grid_for_logic.setObjectName(u"grid_for_logic")
        self.logic_desc = QLabel(self.tab_for_settings)
        self.logic_desc.setObjectName(u"logic_desc")

        self.grid_for_logic.addWidget(self.logic_desc, 1, 1, 1, 3)

        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_logic.addItem(self.left_spacer, 0, 0, 1, 1)

        self.label_for_logic_mod = QLabel(self.tab_for_settings)
        self.label_for_logic_mod.setObjectName(u"label_for_logic_mod")
        self.label_for_logic_mod.setEnabled(True)
        self.label_for_logic_mod.setMaximumSize(QSize(489, 16777215))

        self.grid_for_logic.addWidget(self.label_for_logic_mod, 0, 1, 1, 1)

        self.right_spacer = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_logic.addItem(self.right_spacer, 0, 4, 1, 1)

        self.logic_spacer = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_logic.addItem(self.logic_spacer, 0, 3, 1, 1)

        self.logic_mod = QComboBox(self.tab_for_settings)
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.addItem("")
        self.logic_mod.setObjectName(u"logic_mod")
        self.logic_mod.setMinimumSize(QSize(70, 0))
        self.logic_mod.setDuplicatesEnabled(False)
        self.logic_mod.setFrame(True)

        self.grid_for_logic.addWidget(self.logic_mod, 0, 2, 1, 1)


        self.layout_for_paths.addLayout(self.grid_for_logic)

        self.group_for_locations = QGroupBox(self.tab_for_settings)
        self.group_for_locations.setObjectName(u"group_for_locations")
        self.grid_for_locations = QGridLayout(self.group_for_locations)
        self.grid_for_locations.setObjectName(u"grid_for_locations")
        self.progression_island_puzzles = QCheckBox(self.group_for_locations)
        self.progression_island_puzzles.setObjectName(u"progression_island_puzzles")

        self.grid_for_locations.addWidget(self.progression_island_puzzles, 1, 2, 1, 1)

        self.progression_long_combat_trials = QCheckBox(self.group_for_locations)
        self.progression_long_combat_trials.setObjectName(u"progression_long_combat_trials")

        self.grid_for_locations.addWidget(self.progression_long_combat_trials, 1, 3, 1, 1)

        self.progression_mixed_secret_caves = QCheckBox(self.group_for_locations)
        self.progression_mixed_secret_caves.setObjectName(u"progression_mixed_secret_caves")

        self.grid_for_locations.addWidget(self.progression_mixed_secret_caves, 0, 2, 1, 1)

        self.progression_combat_secret_caves = QCheckBox(self.group_for_locations)
        self.progression_combat_secret_caves.setObjectName(u"progression_combat_secret_caves")

        self.grid_for_locations.addWidget(self.progression_combat_secret_caves, 0, 3, 1, 1)

        self.progression_tingle_chests = QCheckBox(self.group_for_locations)
        self.progression_tingle_chests.setObjectName(u"progression_tingle_chests")

        self.grid_for_locations.addWidget(self.progression_tingle_chests, 1, 0, 1, 1)

        self.progression_big_octos_gunboats = QCheckBox(self.group_for_locations)
        self.progression_big_octos_gunboats.setObjectName(u"progression_big_octos_gunboats")

        self.grid_for_locations.addWidget(self.progression_big_octos_gunboats, 3, 3, 1, 1)

        self.progression_treasure_charts = QCheckBox(self.group_for_locations)
        self.progression_treasure_charts.setObjectName(u"progression_treasure_charts")

        self.grid_for_locations.addWidget(self.progression_treasure_charts, 5, 2, 1, 2)

        self.progression_submarines = QCheckBox(self.group_for_locations)
        self.progression_submarines.setObjectName(u"progression_submarines")
        self.progression_submarines.setChecked(False)

        self.grid_for_locations.addWidget(self.progression_submarines, 4, 0, 1, 1)

        self.progression_platforms_rafts = QCheckBox(self.group_for_locations)
        self.progression_platforms_rafts.setObjectName(u"progression_platforms_rafts")

        self.grid_for_locations.addWidget(self.progression_platforms_rafts, 2, 3, 1, 1)

        self.progression_great_fairies = QCheckBox(self.group_for_locations)
        self.progression_great_fairies.setObjectName(u"progression_great_fairies")
        self.progression_great_fairies.setChecked(True)

        self.grid_for_locations.addWidget(self.progression_great_fairies, 1, 1, 1, 1)

        self.progression_eye_reef_chests = QCheckBox(self.group_for_locations)
        self.progression_eye_reef_chests.setObjectName(u"progression_eye_reef_chests")

        self.grid_for_locations.addWidget(self.progression_eye_reef_chests, 4, 1, 1, 1)

        self.progression_misc = QCheckBox(self.group_for_locations)
        self.progression_misc.setObjectName(u"progression_misc")
        self.progression_misc.setCheckable(True)
        self.progression_misc.setChecked(False)

        self.grid_for_locations.addWidget(self.progression_misc, 4, 3, 1, 1)

        self.progression_puzzle_secret_caves = QCheckBox(self.group_for_locations)
        self.progression_puzzle_secret_caves.setObjectName(u"progression_puzzle_secret_caves")
        self.progression_puzzle_secret_caves.setChecked(True)

        self.grid_for_locations.addWidget(self.progression_puzzle_secret_caves, 0, 1, 1, 1)

        self.progression_spoils_trading = QCheckBox(self.group_for_locations)
        self.progression_spoils_trading.setObjectName(u"progression_spoils_trading")

        self.grid_for_locations.addWidget(self.progression_spoils_trading, 2, 2, 1, 1)

        self.progression_triforce_charts = QCheckBox(self.group_for_locations)
        self.progression_triforce_charts.setObjectName(u"progression_triforce_charts")

        self.grid_for_locations.addWidget(self.progression_triforce_charts, 5, 0, 1, 2)

        self.progression_expensive_purchases = QCheckBox(self.group_for_locations)
        self.progression_expensive_purchases.setObjectName(u"progression_expensive_purchases")
        self.progression_expensive_purchases.setChecked(True)

        self.grid_for_locations.addWidget(self.progression_expensive_purchases, 3, 2, 1, 1)

        self.progression_short_sidequests = QCheckBox(self.group_for_locations)
        self.progression_short_sidequests.setObjectName(u"progression_short_sidequests")
        self.progression_short_sidequests.setChecked(True)

        self.grid_for_locations.addWidget(self.progression_short_sidequests, 2, 0, 1, 1)

        self.progression_long_sidequests = QCheckBox(self.group_for_locations)
        self.progression_long_sidequests.setObjectName(u"progression_long_sidequests")

        self.grid_for_locations.addWidget(self.progression_long_sidequests, 2, 1, 1, 1)

        self.progression_free_gifts = QCheckBox(self.group_for_locations)
        self.progression_free_gifts.setObjectName(u"progression_free_gifts")
        self.progression_free_gifts.setChecked(True)

        self.grid_for_locations.addWidget(self.progression_free_gifts, 4, 2, 1, 1)

        self.progression_short_minigames = QCheckBox(self.group_for_locations)
        self.progression_short_minigames.setObjectName(u"progression_short_minigames")

        self.grid_for_locations.addWidget(self.progression_short_minigames, 3, 0, 1, 1)

        self.progression_dungeons = QCheckBox(self.group_for_locations)
        self.progression_dungeons.setObjectName(u"progression_dungeons")
        self.progression_dungeons.setChecked(True)

        self.grid_for_locations.addWidget(self.progression_dungeons, 0, 0, 1, 1)

        self.progression_long_minigames = QCheckBox(self.group_for_locations)
        self.progression_long_minigames.setObjectName(u"progression_long_minigames")

        self.grid_for_locations.addWidget(self.progression_long_minigames, 3, 1, 1, 1)


        self.layout_for_paths.addWidget(self.group_for_locations)

        self.group_for_settings_secondary = QGroupBox(self.tab_for_settings)
        self.group_for_settings_secondary.setObjectName(u"group_for_settings_secondary")
        self.grid_for_settings_secondary = QGridLayout(self.group_for_settings_secondary)
        self.grid_for_settings_secondary.setObjectName(u"grid_for_settings_secondary")
        self.compass_map_pool_with_keys = QCheckBox(self.group_for_settings_secondary)
        self.compass_map_pool_with_keys.setObjectName(u"compass_map_pool_with_keys")

        self.grid_for_settings_secondary.addWidget(self.compass_map_pool_with_keys, 0, 4, 1, 1)

        self.layout_for_keymode = QHBoxLayout()
        self.layout_for_keymode.setObjectName(u"layout_for_keymode")
        self.label_for_keymode = QLabel(self.group_for_settings_secondary)
        self.label_for_keymode.setObjectName(u"label_for_keymode")

        self.layout_for_keymode.addWidget(self.label_for_keymode)

        self.spacer_for_keymode = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_keymode.addItem(self.spacer_for_keymode)

        self.keymode = QComboBox(self.group_for_settings_secondary)
        self.keymode.addItem("")
        self.keymode.addItem("")
        self.keymode.addItem("")
        self.keymode.setObjectName(u"keymode")

        self.layout_for_keymode.addWidget(self.keymode)

        self.layout_for_keymode.setStretch(0, 2)
        self.layout_for_keymode.setStretch(1, 1)
        self.layout_for_keymode.setStretch(2, 2)

        self.grid_for_settings_secondary.addLayout(self.layout_for_keymode, 0, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_settings_secondary.addItem(self.horizontalSpacer_17, 1, 3, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_settings_secondary.addItem(self.horizontalSpacer_16, 1, 1, 1, 1)

        self.layout_for_sword = QHBoxLayout()
        self.layout_for_sword.setObjectName(u"layout_for_sword")
        self.label_for_sword_mode = QLabel(self.group_for_settings_secondary)
        self.label_for_sword_mode.setObjectName(u"label_for_sword_mode")

        self.layout_for_sword.addWidget(self.label_for_sword_mode)

        self.spacer_for_sword_mode = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_sword.addItem(self.spacer_for_sword_mode)

        self.sword_mode = QComboBox(self.group_for_settings_secondary)
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.setObjectName(u"sword_mode")

        self.layout_for_sword.addWidget(self.sword_mode)

        self.layout_for_sword.setStretch(0, 1)
        self.layout_for_sword.setStretch(2, 1)

        self.grid_for_settings_secondary.addLayout(self.layout_for_sword, 0, 0, 1, 1)

        self.layout_for_starting_triforce_shards = QHBoxLayout()
        self.layout_for_starting_triforce_shards.setObjectName(u"layout_for_starting_triforce_shards")
        self.label_for_num_starting_triforce_shards = QLabel(self.group_for_settings_secondary)
        self.label_for_num_starting_triforce_shards.setObjectName(u"label_for_num_starting_triforce_shards")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_for_num_starting_triforce_shards.sizePolicy().hasHeightForWidth())
        self.label_for_num_starting_triforce_shards.setSizePolicy(sizePolicy1)

        self.layout_for_starting_triforce_shards.addWidget(self.label_for_num_starting_triforce_shards)

        self.spacer_for_num_starting_triforce_shards = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_starting_triforce_shards.addItem(self.spacer_for_num_starting_triforce_shards)

        self.num_starting_triforce_shards = QComboBox(self.group_for_settings_secondary)
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.setObjectName(u"num_starting_triforce_shards")
        self.num_starting_triforce_shards.setMaximumSize(QSize(84, 16777215))

        self.layout_for_starting_triforce_shards.addWidget(self.num_starting_triforce_shards)


        self.grid_for_settings_secondary.addLayout(self.layout_for_starting_triforce_shards, 1, 4, 1, 1)

        self.layout_for_num_dungeon_race_mode = QHBoxLayout()
        self.layout_for_num_dungeon_race_mode.setObjectName(u"layout_for_num_dungeon_race_mode")
        self.label_for_num_dungeon_race_mode = QLabel(self.group_for_settings_secondary)
        self.label_for_num_dungeon_race_mode.setObjectName(u"label_for_num_dungeon_race_mode")
        sizePolicy1.setHeightForWidth(self.label_for_num_dungeon_race_mode.sizePolicy().hasHeightForWidth())
        self.label_for_num_dungeon_race_mode.setSizePolicy(sizePolicy1)

        self.layout_for_num_dungeon_race_mode.addWidget(self.label_for_num_dungeon_race_mode)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_num_dungeon_race_mode.addItem(self.horizontalSpacer_6)

        self.num_dungeon_race_mode = QComboBox(self.group_for_settings_secondary)
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.addItem("")
        self.num_dungeon_race_mode.setObjectName(u"num_dungeon_race_mode")
        self.num_dungeon_race_mode.setMaximumSize(QSize(84, 16777215))

        self.layout_for_num_dungeon_race_mode.addWidget(self.num_dungeon_race_mode)


        self.grid_for_settings_secondary.addLayout(self.layout_for_num_dungeon_race_mode, 1, 2, 1, 1)

        self.layout_for_race_mode = QHBoxLayout()
        self.layout_for_race_mode.setObjectName(u"layout_for_race_mode")
        self.label_for_race_mode = QLabel(self.group_for_settings_secondary)
        self.label_for_race_mode.setObjectName(u"label_for_race_mode")

        self.layout_for_race_mode.addWidget(self.label_for_race_mode)

        self.spacer_for_race_mode = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_race_mode.addItem(self.spacer_for_race_mode)

        self.race_mode = QComboBox(self.group_for_settings_secondary)
        self.race_mode.addItem("")
        self.race_mode.addItem("")
        self.race_mode.addItem("")
        self.race_mode.setObjectName(u"race_mode")

        self.layout_for_race_mode.addWidget(self.race_mode)

        self.layout_for_race_mode.setStretch(0, 1)
        self.layout_for_race_mode.setStretch(2, 2)

        self.grid_for_settings_secondary.addLayout(self.layout_for_race_mode, 1, 0, 1, 1)

        self.add_shortcut_warps_between_dungeons = QCheckBox(self.group_for_settings_secondary)
        self.add_shortcut_warps_between_dungeons.setObjectName(u"add_shortcut_warps_between_dungeons")
        self.add_shortcut_warps_between_dungeons.setChecked(True)

        self.grid_for_settings_secondary.addWidget(self.add_shortcut_warps_between_dungeons, 2, 2, 1, 1)

        self.layout_for_randomize_entrances = QHBoxLayout()
        self.layout_for_randomize_entrances.setObjectName(u"layout_for_randomize_entrances")
        self.label_for_randomize_entrances = QLabel(self.group_for_settings_secondary)
        self.label_for_randomize_entrances.setObjectName(u"label_for_randomize_entrances")

        self.layout_for_randomize_entrances.addWidget(self.label_for_randomize_entrances)

        self.spacer_for_randomize_entrances = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_randomize_entrances.addItem(self.spacer_for_randomize_entrances)

        self.randomize_entrances = QComboBox(self.group_for_settings_secondary)
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.addItem("")
        self.randomize_entrances.setObjectName(u"randomize_entrances")

        self.layout_for_randomize_entrances.addWidget(self.randomize_entrances)

        self.layout_for_randomize_entrances.setStretch(0, 2)
        self.layout_for_randomize_entrances.setStretch(1, 1)
        self.layout_for_randomize_entrances.setStretch(2, 2)

        self.grid_for_settings_secondary.addLayout(self.layout_for_randomize_entrances, 2, 4, 1, 1)


        self.layout_for_paths.addWidget(self.group_for_settings_secondary)

        self.group_for_convenience = QGroupBox(self.tab_for_settings)
        self.group_for_convenience.setObjectName(u"group_for_convenience")
        self.grid_for_convenience = QGridLayout(self.group_for_convenience)
        self.grid_for_convenience.setObjectName(u"grid_for_convenience")
        self.layout_for_can_chain_charts = QHBoxLayout()
        self.layout_for_can_chain_charts.setObjectName(u"layout_for_can_chain_charts")
        self.label_for_can_chain_charts = QLabel(self.group_for_convenience)
        self.label_for_can_chain_charts.setObjectName(u"label_for_can_chain_charts")

        self.layout_for_can_chain_charts.addWidget(self.label_for_can_chain_charts)

        self.spacer_for_can_chain_charts = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_can_chain_charts.addItem(self.spacer_for_can_chain_charts)

        self.can_chain_charts = QComboBox(self.group_for_convenience)
        self.can_chain_charts.addItem("")
        self.can_chain_charts.addItem("")
        self.can_chain_charts.addItem("")
        self.can_chain_charts.setObjectName(u"can_chain_charts")

        self.layout_for_can_chain_charts.addWidget(self.can_chain_charts)

        self.layout_for_can_chain_charts.setStretch(0, 2)
        self.layout_for_can_chain_charts.setStretch(1, 1)
        self.layout_for_can_chain_charts.setStretch(2, 2)

        self.grid_for_convenience.addLayout(self.layout_for_can_chain_charts, 2, 4, 1, 1)

        self.reveal_full_sea_chart = QCheckBox(self.group_for_convenience)
        self.reveal_full_sea_chart.setObjectName(u"reveal_full_sea_chart")
        self.reveal_full_sea_chart.setChecked(True)

        self.grid_for_convenience.addWidget(self.reveal_full_sea_chart, 2, 0, 1, 1)

        self.randomize_charts = QCheckBox(self.group_for_convenience)
        self.randomize_charts.setObjectName(u"randomize_charts")

        self.grid_for_convenience.addWidget(self.randomize_charts, 2, 2, 1, 1)

        self.randomize_starting_island = QCheckBox(self.group_for_convenience)
        self.randomize_starting_island.setObjectName(u"randomize_starting_island")

        self.grid_for_convenience.addWidget(self.randomize_starting_island, 1, 0, 1, 1)

        self.swift_sail = QCheckBox(self.group_for_convenience)
        self.swift_sail.setObjectName(u"swift_sail")
        self.swift_sail.setChecked(True)

        self.grid_for_convenience.addWidget(self.swift_sail, 0, 0, 1, 1)

        self.instant_text_boxes = QCheckBox(self.group_for_convenience)
        self.instant_text_boxes.setObjectName(u"instant_text_boxes")
        self.instant_text_boxes.setChecked(True)

        self.grid_for_convenience.addWidget(self.instant_text_boxes, 0, 2, 1, 1)

        self.skip_rematch_bosses = QCheckBox(self.group_for_convenience)
        self.skip_rematch_bosses.setObjectName(u"skip_rematch_bosses")
        self.skip_rematch_bosses.setChecked(True)

        self.grid_for_convenience.addWidget(self.skip_rematch_bosses, 0, 4, 1, 1)

        self.remove_title_and_ending_videos = QCheckBox(self.group_for_convenience)
        self.remove_title_and_ending_videos.setObjectName(u"remove_title_and_ending_videos")
        self.remove_title_and_ending_videos.setChecked(True)

        self.grid_for_convenience.addWidget(self.remove_title_and_ending_videos, 1, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_convenience.addItem(self.horizontalSpacer_15, 0, 3, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_convenience.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.layout_for_convenience_option = QHBoxLayout()
        self.layout_for_convenience_option.setObjectName(u"layout_for_convenience_option")
        self.convenience_option_label = QLabel(self.group_for_convenience)
        self.convenience_option_label.setObjectName(u"convenience_option_label")

        self.layout_for_convenience_option.addWidget(self.convenience_option_label)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_convenience_option.addItem(self.horizontalSpacer_21)

        self.convenience_option = QComboBox(self.group_for_convenience)
        self.convenience_option.addItem("")
        self.convenience_option.addItem("")
        self.convenience_option.addItem("")
        self.convenience_option.addItem("")
        self.convenience_option.setObjectName(u"convenience_option")

        self.layout_for_convenience_option.addWidget(self.convenience_option)

        self.layout_for_convenience_option.setStretch(0, 2)
        self.layout_for_convenience_option.setStretch(1, 1)
        self.layout_for_convenience_option.setStretch(2, 2)

        self.grid_for_convenience.addLayout(self.layout_for_convenience_option, 1, 4, 1, 1)


        self.layout_for_paths.addWidget(self.group_for_convenience)

        self.group_for_spoiler = QGroupBox(self.tab_for_settings)
        self.group_for_spoiler.setObjectName(u"group_for_spoiler")
        self.grid_for_spoiler = QGridLayout(self.group_for_spoiler)
        self.grid_for_spoiler.setObjectName(u"grid_for_spoiler")
        self.generate_spoiler_log = QCheckBox(self.group_for_spoiler)
        self.generate_spoiler_log.setObjectName(u"generate_spoiler_log")
        self.generate_spoiler_log.setChecked(False)

        self.grid_for_spoiler.addWidget(self.generate_spoiler_log, 0, 0, 1, 1)

        self.progression_check_spoiler_log = QCheckBox(self.group_for_spoiler)
        self.progression_check_spoiler_log.setObjectName(u"progression_check_spoiler_log")
        self.progression_check_spoiler_log.setChecked(True)

        self.grid_for_spoiler.addWidget(self.progression_check_spoiler_log, 1, 0, 1, 1)

        self.all_check_spoiler_log = QCheckBox(self.group_for_spoiler)
        self.all_check_spoiler_log.setObjectName(u"all_check_spoiler_log")
        self.all_check_spoiler_log.setChecked(True)

        self.grid_for_spoiler.addWidget(self.all_check_spoiler_log, 1, 1, 1, 1)

        self.entrance_spoiler_log = QCheckBox(self.group_for_spoiler)
        self.entrance_spoiler_log.setObjectName(u"entrance_spoiler_log")
        self.entrance_spoiler_log.setChecked(True)

        self.grid_for_spoiler.addWidget(self.entrance_spoiler_log, 1, 2, 1, 1)

        self.chart_spoiler_log = QCheckBox(self.group_for_spoiler)
        self.chart_spoiler_log.setObjectName(u"chart_spoiler_log")
        self.chart_spoiler_log.setChecked(True)

        self.grid_for_spoiler.addWidget(self.chart_spoiler_log, 1, 3, 1, 1)


        self.layout_for_paths.addWidget(self.group_for_spoiler)

        self.group_for_advanced = QGroupBox(self.tab_for_settings)
        self.group_for_advanced.setObjectName(u"group_for_advanced")
        self.grid_for_advanced = QGridLayout(self.group_for_advanced)
        self.grid_for_advanced.setObjectName(u"grid_for_advanced")
        self.widget_4 = QWidget(self.group_for_advanced)
        self.widget_4.setObjectName(u"widget_4")

        self.grid_for_advanced.addWidget(self.widget_4, 0, 6, 1, 1)

        self.widget_3 = QWidget(self.group_for_advanced)
        self.widget_3.setObjectName(u"widget_3")

        self.grid_for_advanced.addWidget(self.widget_3, 0, 5, 1, 1)

        self.invert_camera_x_axis = QCheckBox(self.group_for_advanced)
        self.invert_camera_x_axis.setObjectName(u"invert_camera_x_axis")

        self.grid_for_advanced.addWidget(self.invert_camera_x_axis, 0, 4, 1, 1)

        self.randomize_enemies = QCheckBox(self.group_for_advanced)
        self.randomize_enemies.setObjectName(u"randomize_enemies")
        self.randomize_enemies.setEnabled(False)

        self.grid_for_advanced.addWidget(self.randomize_enemies, 1, 2, 1, 1)

        self.disable_tingle_chests_with_tingle_bombs = QCheckBox(self.group_for_advanced)
        self.disable_tingle_chests_with_tingle_bombs.setObjectName(u"disable_tingle_chests_with_tingle_bombs")
        self.disable_tingle_chests_with_tingle_bombs.setEnabled(False)
        self.disable_tingle_chests_with_tingle_bombs.setChecked(True)

        self.grid_for_advanced.addWidget(self.disable_tingle_chests_with_tingle_bombs, 1, 4, 1, 1)

        self.randomize_enemy_palettes = QCheckBox(self.group_for_advanced)
        self.randomize_enemy_palettes.setObjectName(u"randomize_enemy_palettes")
        self.randomize_enemy_palettes.setEnabled(True)

        self.grid_for_advanced.addWidget(self.randomize_enemy_palettes, 0, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_advanced.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.randomize_music = QCheckBox(self.group_for_advanced)
        self.randomize_music.setObjectName(u"randomize_music")
        self.randomize_music.setEnabled(True)

        self.grid_for_advanced.addWidget(self.randomize_music, 1, 0, 1, 1)

        self.remove_music = QCheckBox(self.group_for_advanced)
        self.remove_music.setObjectName(u"remove_music")

        self.grid_for_advanced.addWidget(self.remove_music, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.grid_for_advanced.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)


        self.layout_for_paths.addWidget(self.group_for_advanced)

        self.tab_for_main.addTab(self.tab_for_settings, "")
        self.tab_for_starting_items = QWidget()
        self.tab_for_starting_items.setObjectName(u"tab_for_starting_items")
        self.tab_for_starting_items.setEnabled(True)
        self.layout_for_items_selection = QVBoxLayout(self.tab_for_starting_items)
        self.layout_for_items_selection.setObjectName(u"layout_for_items_selection")
        self.layout_for_starting_items = QHBoxLayout()
        self.layout_for_starting_items.setObjectName(u"layout_for_starting_items")
        self.layout_for_randomized_gear = QVBoxLayout()
        self.layout_for_randomized_gear.setObjectName(u"layout_for_randomized_gear")
        self.label_for_randomized_gear = QLabel(self.tab_for_starting_items)
        self.label_for_randomized_gear.setObjectName(u"label_for_randomized_gear")

        self.layout_for_randomized_gear.addWidget(self.label_for_randomized_gear)

        self.randomized_gear = QListView(self.tab_for_starting_items)
        self.randomized_gear.setObjectName(u"randomized_gear")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.randomized_gear.sizePolicy().hasHeightForWidth())
        self.randomized_gear.setSizePolicy(sizePolicy2)
        self.randomized_gear.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.randomized_gear.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layout_for_randomized_gear.addWidget(self.randomized_gear)


        self.layout_for_starting_items.addLayout(self.layout_for_randomized_gear)

        self.layout_for_gear_options = QVBoxLayout()
        self.layout_for_gear_options.setObjectName(u"layout_for_gear_options")
        self.spacer_for_options_gear_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.layout_for_gear_options.addItem(self.spacer_for_options_gear_top)

        self.remove_gear = QPushButton(self.tab_for_starting_items)
        self.remove_gear.setObjectName(u"remove_gear")
        self.remove_gear.setMinimumSize(QSize(60, 80))

        self.layout_for_gear_options.addWidget(self.remove_gear)

        self.add_gear = QPushButton(self.tab_for_starting_items)
        self.add_gear.setObjectName(u"add_gear")
        self.add_gear.setMinimumSize(QSize(60, 80))

        self.layout_for_gear_options.addWidget(self.add_gear)

        self.spacer_for_options_gear_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.layout_for_gear_options.addItem(self.spacer_for_options_gear_bottom)


        self.layout_for_starting_items.addLayout(self.layout_for_gear_options)

        self.layout_for_starting_gear = QVBoxLayout()
        self.layout_for_starting_gear.setObjectName(u"layout_for_starting_gear")
        self.label_for_starting_gear = QLabel(self.tab_for_starting_items)
        self.label_for_starting_gear.setObjectName(u"label_for_starting_gear")

        self.layout_for_starting_gear.addWidget(self.label_for_starting_gear)

        self.starting_gear = QListView(self.tab_for_starting_items)
        self.starting_gear.setObjectName(u"starting_gear")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.starting_gear.sizePolicy().hasHeightForWidth())
        self.starting_gear.setSizePolicy(sizePolicy3)
        self.starting_gear.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.starting_gear.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layout_for_starting_gear.addWidget(self.starting_gear)


        self.layout_for_starting_items.addLayout(self.layout_for_starting_gear)


        self.layout_for_items_selection.addLayout(self.layout_for_starting_items)

        self.layout_for_additional_starting = QHBoxLayout()
        self.layout_for_additional_starting.setObjectName(u"layout_for_additional_starting")
        self.label_for_additional_starting_min = QLabel(self.tab_for_starting_items)
        self.label_for_additional_starting_min.setObjectName(u"label_for_additional_starting_min")

        self.layout_for_additional_starting.addWidget(self.label_for_additional_starting_min)

        self.additional_starting_min = QSpinBox(self.tab_for_starting_items)
        self.additional_starting_min.setObjectName(u"additional_starting_min")
        self.additional_starting_min.setMaximum(47)

        self.layout_for_additional_starting.addWidget(self.additional_starting_min)

        self.label_for_additional_starting_max = QLabel(self.tab_for_starting_items)
        self.label_for_additional_starting_max.setObjectName(u"label_for_additional_starting_max")

        self.layout_for_additional_starting.addWidget(self.label_for_additional_starting_max)

        self.additional_starting_max = QSpinBox(self.tab_for_starting_items)
        self.additional_starting_max.setObjectName(u"additional_starting_max")
        self.additional_starting_max.setMaximum(47)

        self.layout_for_additional_starting.addWidget(self.additional_starting_max)

        self.label_for_additional_starting = QLabel(self.tab_for_starting_items)
        self.label_for_additional_starting.setObjectName(u"label_for_additional_starting")

        self.layout_for_additional_starting.addWidget(self.label_for_additional_starting)

        self.spacer_for_additional_starting = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_additional_starting.addItem(self.spacer_for_additional_starting)

        self.text_for_total_starting_min = QLabel(self.tab_for_starting_items)
        self.text_for_total_starting_min.setObjectName(u"text_for_total_starting_min")

        self.layout_for_additional_starting.addWidget(self.text_for_total_starting_min)

        self.label_for_total_starting = QLabel(self.tab_for_starting_items)
        self.label_for_total_starting.setObjectName(u"label_for_total_starting")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_for_total_starting.setFont(font)

        self.layout_for_additional_starting.addWidget(self.label_for_total_starting)

        self.text_for_total_starting_max = QLabel(self.tab_for_starting_items)
        self.text_for_total_starting_max.setObjectName(u"text_for_total_starting_max")

        self.layout_for_additional_starting.addWidget(self.text_for_total_starting_max)


        self.layout_for_items_selection.addLayout(self.layout_for_additional_starting)

        self.layout_for_starting_health = QHBoxLayout()
        self.layout_for_starting_health.setObjectName(u"layout_for_starting_health")
        self.label_for_starting_bh = QLabel(self.tab_for_starting_items)
        self.label_for_starting_bh.setObjectName(u"label_for_starting_bh")

        self.layout_for_starting_health.addWidget(self.label_for_starting_bh)

        self.starting_bh = QSpinBox(self.tab_for_starting_items)
        self.starting_bh.setObjectName(u"starting_bh")
        self.starting_bh.setMinimum(1)
        self.starting_bh.setMaximum(3)
        self.starting_bh.setValue(3)

        self.layout_for_starting_health.addWidget(self.starting_bh)

        self.label_for_starting_hcs = QLabel(self.tab_for_starting_items)
        self.label_for_starting_hcs.setObjectName(u"label_for_starting_hcs")

        self.layout_for_starting_health.addWidget(self.label_for_starting_hcs)

        self.starting_hcs = QSpinBox(self.tab_for_starting_items)
        self.starting_hcs.setObjectName(u"starting_hcs")
        self.starting_hcs.setEnabled(True)
        self.starting_hcs.setBaseSize(QSize(0, 0))
        self.starting_hcs.setLayoutDirection(Qt.LeftToRight)
        self.starting_hcs.setMaximum(6)
        self.starting_hcs.setValue(0)
        self.starting_hcs.setDisplayIntegerBase(10)

        self.layout_for_starting_health.addWidget(self.starting_hcs)

        self.label_for_starting_pohs = QLabel(self.tab_for_starting_items)
        self.label_for_starting_pohs.setObjectName(u"label_for_starting_pohs")
        sizePolicy.setHeightForWidth(self.label_for_starting_pohs.sizePolicy().hasHeightForWidth())
        self.label_for_starting_pohs.setSizePolicy(sizePolicy)

        self.layout_for_starting_health.addWidget(self.label_for_starting_pohs)

        self.starting_pohs = QSpinBox(self.tab_for_starting_items)
        self.starting_pohs.setObjectName(u"starting_pohs")
        self.starting_pohs.setMaximum(44)
        self.starting_pohs.setValue(0)
        self.starting_pohs.setDisplayIntegerBase(10)

        self.layout_for_starting_health.addWidget(self.starting_pohs)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_starting_health.addItem(self.horizontalSpacer)

        self.current_health = QLabel(self.tab_for_starting_items)
        self.current_health.setObjectName(u"current_health")

        self.layout_for_starting_health.addWidget(self.current_health)

        self.spacer_for_health_end = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_starting_health.addItem(self.spacer_for_health_end)

        self.no_heart_in_pool = QCheckBox(self.tab_for_starting_items)
        self.no_heart_in_pool.setObjectName(u"no_heart_in_pool")

        self.layout_for_starting_health.addWidget(self.no_heart_in_pool)


        self.layout_for_items_selection.addLayout(self.layout_for_starting_health)

        self.spacer_below_starting_health = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_items_selection.addItem(self.spacer_below_starting_health)

        self.layout_for_items_selection.setStretch(0, 20)
        self.layout_for_items_selection.setStretch(3, 1)
        self.tab_for_main.addTab(self.tab_for_starting_items, "")
        self.tab_for_entrances = QWidget()
        self.tab_for_entrances.setObjectName(u"tab_for_entrances")
        self.tab_for_entrances.setEnabled(True)
        self.layout_for_entrance_selection = QVBoxLayout(self.tab_for_entrances)
        self.layout_for_entrance_selection.setObjectName(u"layout_for_entrance_selection")
        self.layout_for_entrance_fields = QHBoxLayout()
        self.layout_for_entrance_fields.setObjectName(u"layout_for_entrance_fields")
        self.layout_for_vanilla_entrances = QVBoxLayout()
        self.layout_for_vanilla_entrances.setObjectName(u"layout_for_vanilla_entrances")
        self.label_for_vanilla_entrances = QLabel(self.tab_for_entrances)
        self.label_for_vanilla_entrances.setObjectName(u"label_for_vanilla_entrances")

        self.layout_for_vanilla_entrances.addWidget(self.label_for_vanilla_entrances)

        self.vanilla_entrances = QListView(self.tab_for_entrances)
        self.vanilla_entrances.setObjectName(u"vanilla_entrances")

        self.layout_for_vanilla_entrances.addWidget(self.vanilla_entrances)


        self.layout_for_entrance_fields.addLayout(self.layout_for_vanilla_entrances)

        self.layout_for_to_non_vanilla_options = QVBoxLayout()
        self.layout_for_to_non_vanilla_options.setObjectName(u"layout_for_to_non_vanilla_options")
        self.space_non_vanilla_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_to_non_vanilla_options.addItem(self.space_non_vanilla_top)

        self.add_vanilla_from_limited = QPushButton(self.tab_for_entrances)
        self.add_vanilla_from_limited.setObjectName(u"add_vanilla_from_limited")
        self.add_vanilla_from_limited.setMinimumSize(QSize(60, 80))

        self.layout_for_to_non_vanilla_options.addWidget(self.add_vanilla_from_limited)

        self.add_limited_from_vanilla = QPushButton(self.tab_for_entrances)
        self.add_limited_from_vanilla.setObjectName(u"add_limited_from_vanilla")
        self.add_limited_from_vanilla.setMinimumSize(QSize(60, 80))

        self.layout_for_to_non_vanilla_options.addWidget(self.add_limited_from_vanilla)

        self.space_non_vanilla_mid = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_to_non_vanilla_options.addItem(self.space_non_vanilla_mid)

        self.add_vanilla_from_full = QPushButton(self.tab_for_entrances)
        self.add_vanilla_from_full.setObjectName(u"add_vanilla_from_full")
        self.add_vanilla_from_full.setMinimumSize(QSize(60, 80))

        self.layout_for_to_non_vanilla_options.addWidget(self.add_vanilla_from_full)

        self.add_full_from_vanilla = QPushButton(self.tab_for_entrances)
        self.add_full_from_vanilla.setObjectName(u"add_full_from_vanilla")
        self.add_full_from_vanilla.setMinimumSize(QSize(60, 80))

        self.layout_for_to_non_vanilla_options.addWidget(self.add_full_from_vanilla)

        self.space_non_vanilla_bot = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_to_non_vanilla_options.addItem(self.space_non_vanilla_bot)


        self.layout_for_entrance_fields.addLayout(self.layout_for_to_non_vanilla_options)

        self.layout_for_randomized_entrances = QVBoxLayout()
        self.layout_for_randomized_entrances.setObjectName(u"layout_for_randomized_entrances")
        self.layout_for_limited_entrances = QVBoxLayout()
        self.layout_for_limited_entrances.setObjectName(u"layout_for_limited_entrances")
        self.label_for_limited_entrances = QLabel(self.tab_for_entrances)
        self.label_for_limited_entrances.setObjectName(u"label_for_limited_entrances")

        self.layout_for_limited_entrances.addWidget(self.label_for_limited_entrances)

        self.limited_entrances = QListView(self.tab_for_entrances)
        self.limited_entrances.setObjectName(u"limited_entrances")

        self.layout_for_limited_entrances.addWidget(self.limited_entrances)


        self.layout_for_randomized_entrances.addLayout(self.layout_for_limited_entrances)

        self.layout_for_between_random_entrances = QHBoxLayout()
        self.layout_for_between_random_entrances.setObjectName(u"layout_for_between_random_entrances")
        self.spacer_for_limited_from_full = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_between_random_entrances.addItem(self.spacer_for_limited_from_full)

        self.add_limited_from_full = QPushButton(self.tab_for_entrances)
        self.add_limited_from_full.setObjectName(u"add_limited_from_full")
        self.add_limited_from_full.setMinimumSize(QSize(80, 60))

        self.layout_for_between_random_entrances.addWidget(self.add_limited_from_full)

        self.add_full_from_limited = QPushButton(self.tab_for_entrances)
        self.add_full_from_limited.setObjectName(u"add_full_from_limited")
        self.add_full_from_limited.setMinimumSize(QSize(80, 60))

        self.layout_for_between_random_entrances.addWidget(self.add_full_from_limited)

        self.spacer_for_full_from_limited = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_between_random_entrances.addItem(self.spacer_for_full_from_limited)

        self.layout_for_between_random_entrances.setStretch(0, 2)
        self.layout_for_between_random_entrances.setStretch(1, 2)
        self.layout_for_between_random_entrances.setStretch(2, 2)
        self.layout_for_between_random_entrances.setStretch(3, 3)

        self.layout_for_randomized_entrances.addLayout(self.layout_for_between_random_entrances)

        self.layout_for_full_entrances = QVBoxLayout()
        self.layout_for_full_entrances.setObjectName(u"layout_for_full_entrances")
        self.label_for_full_entrances = QLabel(self.tab_for_entrances)
        self.label_for_full_entrances.setObjectName(u"label_for_full_entrances")

        self.layout_for_full_entrances.addWidget(self.label_for_full_entrances)

        self.full_entrances = QListView(self.tab_for_entrances)
        self.full_entrances.setObjectName(u"full_entrances")

        self.layout_for_full_entrances.addWidget(self.full_entrances)


        self.layout_for_randomized_entrances.addLayout(self.layout_for_full_entrances)

        self.layout_for_randomized_entrances.setStretch(0, 2)
        self.layout_for_randomized_entrances.setStretch(2, 2)

        self.layout_for_entrance_fields.addLayout(self.layout_for_randomized_entrances)


        self.layout_for_entrance_selection.addLayout(self.layout_for_entrance_fields)

        self.layout_for_entrance_selection.setStretch(0, 20)
        self.tab_for_main.addTab(self.tab_for_entrances, "")
        self.tab_for_locales = QWidget()
        self.tab_for_locales.setObjectName(u"tab_for_locales")
        self.layout_for_locales = QVBoxLayout(self.tab_for_locales)
        self.layout_for_locales.setObjectName(u"layout_for_locales")
        self.grid_for_locales = QGridLayout()
        self.grid_for_locales.setObjectName(u"grid_for_locales")
        self.locale_stone_watcher = QCheckBox(self.tab_for_locales)
        self.locale_stone_watcher.setObjectName(u"locale_stone_watcher")

        self.grid_for_locales.addWidget(self.locale_stone_watcher, 4, 2, 1, 1)

        self.locale_dvim = QCheckBox(self.tab_for_locales)
        self.locale_dvim.setObjectName(u"locale_dvim")

        self.grid_for_locales.addWidget(self.locale_dvim, 7, 1, 1, 1)

        self.locale_six_eye = QCheckBox(self.tab_for_locales)
        self.locale_six_eye.setObjectName(u"locale_six_eye")

        self.grid_for_locales.addWidget(self.locale_six_eye, 3, 3, 1, 1)

        self.locale_picto = QCheckBox(self.tab_for_locales)
        self.locale_picto.setObjectName(u"locale_picto")

        self.grid_for_locales.addWidget(self.locale_picto, 7, 3, 1, 1)

        self.locale_southern_triangle = QCheckBox(self.tab_for_locales)
        self.locale_southern_triangle.setObjectName(u"locale_southern_triangle")

        self.grid_for_locales.addWidget(self.locale_southern_triangle, 4, 3, 1, 1)

        self.locale_bomb = QCheckBox(self.tab_for_locales)
        self.locale_bomb.setObjectName(u"locale_bomb")

        self.grid_for_locales.addWidget(self.locale_bomb, 4, 5, 1, 1)

        self.locale_ff = QCheckBox(self.tab_for_locales)
        self.locale_ff.setObjectName(u"locale_ff")

        self.grid_for_locales.addWidget(self.locale_ff, 0, 0, 1, 1)

        self.locale_five_eye = QCheckBox(self.tab_for_locales)
        self.locale_five_eye.setObjectName(u"locale_five_eye")

        self.grid_for_locales.addWidget(self.locale_five_eye, 5, 1, 1, 1)

        self.locale_boating_course = QCheckBox(self.tab_for_locales)
        self.locale_boating_course.setObjectName(u"locale_boating_course")

        self.grid_for_locales.addWidget(self.locale_boating_course, 6, 5, 1, 1)

        self.locale_spectacle = QCheckBox(self.tab_for_locales)
        self.locale_spectacle.setObjectName(u"locale_spectacle")

        self.grid_for_locales.addWidget(self.locale_spectacle, 1, 2, 1, 1)

        self.locale_forest_haven = QCheckBox(self.tab_for_locales)
        self.locale_forest_haven.setObjectName(u"locale_forest_haven")

        self.grid_for_locales.addWidget(self.locale_forest_haven, 5, 5, 1, 1)

        self.locale_angular = QCheckBox(self.tab_for_locales)
        self.locale_angular.setObjectName(u"locale_angular")

        self.grid_for_locales.addWidget(self.locale_angular, 6, 4, 1, 1)

        self.locale_seven_star = QCheckBox(self.tab_for_locales)
        self.locale_seven_star.setObjectName(u"locale_seven_star")

        self.grid_for_locales.addWidget(self.locale_seven_star, 0, 5, 1, 1)

        self.locale_eastern_fairy = QCheckBox(self.tab_for_locales)
        self.locale_eastern_fairy.setObjectName(u"locale_eastern_fairy")

        self.grid_for_locales.addWidget(self.locale_eastern_fairy, 2, 4, 1, 1)

        self.locale_four_eye = QCheckBox(self.tab_for_locales)
        self.locale_four_eye.setObjectName(u"locale_four_eye")

        self.grid_for_locales.addWidget(self.locale_four_eye, 1, 0, 1, 1)

        self.locale_star = QCheckBox(self.tab_for_locales)
        self.locale_star.setObjectName(u"locale_star")

        self.grid_for_locales.addWidget(self.locale_star, 0, 1, 1, 1)

        self.locale_tingle = QCheckBox(self.tab_for_locales)
        self.locale_tingle.setObjectName(u"locale_tingle")

        self.grid_for_locales.addWidget(self.locale_tingle, 2, 2, 1, 1)

        self.locale_crescent = QCheckBox(self.tab_for_locales)
        self.locale_crescent.setObjectName(u"locale_crescent")

        self.grid_for_locales.addWidget(self.locale_crescent, 0, 4, 1, 1)

        self.locale_western_fairy = QCheckBox(self.tab_for_locales)
        self.locale_western_fairy.setObjectName(u"locale_western_fairy")

        self.grid_for_locales.addWidget(self.locale_western_fairy, 2, 0, 1, 1)

        self.locale_shark = QCheckBox(self.tab_for_locales)
        self.locale_shark.setObjectName(u"locale_shark")

        self.grid_for_locales.addWidget(self.locale_shark, 5, 2, 1, 1)

        self.locale_gale = QCheckBox(self.tab_for_locales)
        self.locale_gale.setObjectName(u"locale_gale")

        self.grid_for_locales.addWidget(self.locale_gale, 0, 3, 1, 1)

        self.locale_fire_mountain = QCheckBox(self.tab_for_locales)
        self.locale_fire_mountain.setObjectName(u"locale_fire_mountain")

        self.grid_for_locales.addWidget(self.locale_fire_mountain, 2, 5, 1, 1)

        self.locale_private_oasis = QCheckBox(self.tab_for_locales)
        self.locale_private_oasis.setObjectName(u"locale_private_oasis")

        self.grid_for_locales.addWidget(self.locale_private_oasis, 4, 4, 1, 1)

        self.locale_overlook = QCheckBox(self.tab_for_locales)
        self.locale_overlook.setObjectName(u"locale_overlook")

        self.grid_for_locales.addWidget(self.locale_overlook, 0, 6, 1, 1)

        self.locale_greatfish = QCheckBox(self.tab_for_locales)
        self.locale_greatfish.setObjectName(u"locale_greatfish")

        self.grid_for_locales.addWidget(self.locale_greatfish, 3, 1, 1, 1)

        self.locale_northern_triangle = QCheckBox(self.tab_for_locales)
        self.locale_northern_triangle.setObjectName(u"locale_northern_triangle")

        self.grid_for_locales.addWidget(self.locale_northern_triangle, 2, 3, 1, 1)

        self.locale_two_eye = QCheckBox(self.tab_for_locales)
        self.locale_two_eye.setObjectName(u"locale_two_eye")

        self.grid_for_locales.addWidget(self.locale_two_eye, 6, 3, 1, 1)

        self.locale_five_star = QCheckBox(self.tab_for_locales)
        self.locale_five_star.setObjectName(u"locale_five_star")

        self.grid_for_locales.addWidget(self.locale_five_star, 6, 6, 1, 1)

        self.locale_savage = QCheckBox(self.tab_for_locales)
        self.locale_savage.setObjectName(u"locale_savage")
        self.locale_savage.setChecked(True)

        self.grid_for_locales.addWidget(self.locale_savage, 7, 5, 1, 1)

        self.locale_rock_spire = QCheckBox(self.tab_for_locales)
        self.locale_rock_spire.setObjectName(u"locale_rock_spire")

        self.grid_for_locales.addWidget(self.locale_rock_spire, 2, 1, 1, 1)

        self.locale_star_belt = QCheckBox(self.tab_for_locales)
        self.locale_star_belt.setObjectName(u"locale_star_belt")

        self.grid_for_locales.addWidget(self.locale_star_belt, 2, 6, 1, 1)

        self.locale_dragon_roost_island = QCheckBox(self.tab_for_locales)
        self.locale_dragon_roost_island.setObjectName(u"locale_dragon_roost_island")

        self.grid_for_locales.addWidget(self.locale_dragon_roost_island, 1, 5, 1, 1)

        self.locale_mother_child = QCheckBox(self.tab_for_locales)
        self.locale_mother_child.setObjectName(u"locale_mother_child")

        self.grid_for_locales.addWidget(self.locale_mother_child, 1, 1, 1, 1)

        self.locale_windfall = QCheckBox(self.tab_for_locales)
        self.locale_windfall.setObjectName(u"locale_windfall")

        self.grid_for_locales.addWidget(self.locale_windfall, 1, 3, 1, 1)

        self.locale_pawprint = QCheckBox(self.tab_for_locales)
        self.locale_pawprint.setObjectName(u"locale_pawprint")

        self.grid_for_locales.addWidget(self.locale_pawprint, 1, 4, 1, 1)

        self.locale_ice_ring = QCheckBox(self.tab_for_locales)
        self.locale_ice_ring.setObjectName(u"locale_ice_ring")

        self.grid_for_locales.addWidget(self.locale_ice_ring, 5, 4, 1, 1)

        self.locale_birds_peak = QCheckBox(self.tab_for_locales)
        self.locale_birds_peak.setObjectName(u"locale_birds_peak")

        self.grid_for_locales.addWidget(self.locale_birds_peak, 4, 6, 1, 1)

        self.locale_flight_control = QCheckBox(self.tab_for_locales)
        self.locale_flight_control.setObjectName(u"locale_flight_control")

        self.grid_for_locales.addWidget(self.locale_flight_control, 1, 6, 1, 1)

        self.locale_cyclops = QCheckBox(self.tab_for_locales)
        self.locale_cyclops.setObjectName(u"locale_cyclops")

        self.grid_for_locales.addWidget(self.locale_cyclops, 3, 2, 1, 1)

        self.locale_southern_fairy = QCheckBox(self.tab_for_locales)
        self.locale_southern_fairy.setObjectName(u"locale_southern_fairy")

        self.grid_for_locales.addWidget(self.locale_southern_fairy, 5, 3, 1, 1)

        self.locale_headstone = QCheckBox(self.tab_for_locales)
        self.locale_headstone.setObjectName(u"locale_headstone")

        self.grid_for_locales.addWidget(self.locale_headstone, 6, 2, 1, 1)

        self.locale_eastern_triangle = QCheckBox(self.tab_for_locales)
        self.locale_eastern_triangle.setObjectName(u"locale_eastern_triangle")

        self.grid_for_locales.addWidget(self.locale_eastern_triangle, 3, 5, 1, 1)

        self.locale_outset = QCheckBox(self.tab_for_locales)
        self.locale_outset.setObjectName(u"locale_outset")

        self.grid_for_locales.addWidget(self.locale_outset, 6, 1, 1, 1)

        self.locale_thorned_fairy = QCheckBox(self.tab_for_locales)
        self.locale_thorned_fairy.setObjectName(u"locale_thorned_fairy")

        self.grid_for_locales.addWidget(self.locale_thorned_fairy, 3, 6, 1, 1)

        self.locale_northern_fairy = QCheckBox(self.tab_for_locales)
        self.locale_northern_fairy.setObjectName(u"locale_northern_fairy")

        self.grid_for_locales.addWidget(self.locale_northern_fairy, 0, 2, 1, 1)

        self.locale_islet = QCheckBox(self.tab_for_locales)
        self.locale_islet.setObjectName(u"locale_islet")

        self.grid_for_locales.addWidget(self.locale_islet, 4, 1, 1, 1)

        self.locale_three_eye = QCheckBox(self.tab_for_locales)
        self.locale_three_eye.setObjectName(u"locale_three_eye")

        self.grid_for_locales.addWidget(self.locale_three_eye, 3, 0, 1, 1)

        self.locale_cliff_plateau = QCheckBox(self.tab_for_locales)
        self.locale_cliff_plateau.setObjectName(u"locale_cliff_plateau")

        self.grid_for_locales.addWidget(self.locale_cliff_plateau, 5, 6, 1, 1)

        self.locale_mail = QCheckBox(self.tab_for_locales)
        self.locale_mail.setObjectName(u"locale_mail")

        self.grid_for_locales.addWidget(self.locale_mail, 7, 2, 1, 1)

        self.locale_needle_rock = QCheckBox(self.tab_for_locales)
        self.locale_needle_rock.setObjectName(u"locale_needle_rock")

        self.grid_for_locales.addWidget(self.locale_needle_rock, 4, 0, 1, 1)

        self.locale_horseshoe = QCheckBox(self.tab_for_locales)
        self.locale_horseshoe.setObjectName(u"locale_horseshoe")

        self.grid_for_locales.addWidget(self.locale_horseshoe, 6, 0, 1, 1)

        self.locale_diamond_steppe = QCheckBox(self.tab_for_locales)
        self.locale_diamond_steppe.setObjectName(u"locale_diamond_steppe")

        self.grid_for_locales.addWidget(self.locale_diamond_steppe, 5, 0, 1, 1)

        self.locale_battlesquid = QCheckBox(self.tab_for_locales)
        self.locale_battlesquid.setObjectName(u"locale_battlesquid")
        self.locale_battlesquid.setChecked(True)

        self.grid_for_locales.addWidget(self.locale_battlesquid, 7, 4, 1, 1)


        self.layout_for_locales.addLayout(self.grid_for_locales)

        self.grid_for_locales1 = QGridLayout()
        self.grid_for_locales1.setObjectName(u"grid_for_locales1")
        self.locale_deep_et = QCheckBox(self.tab_for_locales)
        self.locale_deep_et.setObjectName(u"locale_deep_et")

        self.grid_for_locales1.addWidget(self.locale_deep_et, 1, 4, 1, 1)

        self.locale_et = QCheckBox(self.tab_for_locales)
        self.locale_et.setObjectName(u"locale_et")

        self.grid_for_locales1.addWidget(self.locale_et, 0, 4, 1, 1)

        self.locale_wt = QCheckBox(self.tab_for_locales)
        self.locale_wt.setObjectName(u"locale_wt")

        self.grid_for_locales1.addWidget(self.locale_wt, 0, 5, 1, 1)

        self.locale_drc = QCheckBox(self.tab_for_locales)
        self.locale_drc.setObjectName(u"locale_drc")

        self.grid_for_locales1.addWidget(self.locale_drc, 0, 1, 1, 1)

        self.locale_totg = QCheckBox(self.tab_for_locales)
        self.locale_totg.setObjectName(u"locale_totg")

        self.grid_for_locales1.addWidget(self.locale_totg, 0, 3, 1, 1)

        self.locale_fw = QCheckBox(self.tab_for_locales)
        self.locale_fw.setObjectName(u"locale_fw")

        self.grid_for_locales1.addWidget(self.locale_fw, 0, 2, 1, 1)

        self.locale_under_great_sea = QCheckBox(self.tab_for_locales)
        self.locale_under_great_sea.setObjectName(u"locale_under_great_sea")

        self.grid_for_locales1.addWidget(self.locale_under_great_sea, 1, 0, 1, 1)

        self.locale_great_sea = QCheckBox(self.tab_for_locales)
        self.locale_great_sea.setObjectName(u"locale_great_sea")

        self.grid_for_locales1.addWidget(self.locale_great_sea, 0, 0, 1, 1)

        self.locale_deep_drc = QCheckBox(self.tab_for_locales)
        self.locale_deep_drc.setObjectName(u"locale_deep_drc")

        self.grid_for_locales1.addWidget(self.locale_deep_drc, 1, 1, 1, 1)

        self.locale_deep_fw = QCheckBox(self.tab_for_locales)
        self.locale_deep_fw.setObjectName(u"locale_deep_fw")

        self.grid_for_locales1.addWidget(self.locale_deep_fw, 1, 2, 1, 1)

        self.locale_deep_totg = QCheckBox(self.tab_for_locales)
        self.locale_deep_totg.setObjectName(u"locale_deep_totg")

        self.grid_for_locales1.addWidget(self.locale_deep_totg, 1, 3, 1, 1)

        self.locale_deep_wt = QCheckBox(self.tab_for_locales)
        self.locale_deep_wt.setObjectName(u"locale_deep_wt")

        self.grid_for_locales1.addWidget(self.locale_deep_wt, 1, 5, 1, 1)


        self.layout_for_locales.addLayout(self.grid_for_locales1)

        self.spacer_for_locale = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.layout_for_locales.addItem(self.spacer_for_locale)

        self.layout_for_locales.setStretch(0, 9)
        self.layout_for_locales.setStretch(1, 3)
        self.layout_for_locales.setStretch(2, 6)
        self.tab_for_main.addTab(self.tab_for_locales, "")
        self.tab_for_model_customization = QWidget()
        self.tab_for_model_customization.setObjectName(u"tab_for_model_customization")
        self.layout_for_customization = QVBoxLayout(self.tab_for_model_customization)
        self.layout_for_customization.setObjectName(u"layout_for_customization")
        self.grid_for_model_general_options = QGridLayout()
        self.grid_for_model_general_options.setObjectName(u"grid_for_model_general_options")
        self.layout_for_custom_player_model = QHBoxLayout()
        self.layout_for_custom_player_model.setObjectName(u"layout_for_custom_player_model")
        self.label_for_custom_player_model = QLabel(self.tab_for_model_customization)
        self.label_for_custom_player_model.setObjectName(u"label_for_custom_player_model")

        self.layout_for_custom_player_model.addWidget(self.label_for_custom_player_model)

        self.custom_player_model = QComboBox(self.tab_for_model_customization)
        self.custom_player_model.setObjectName(u"custom_player_model")

        self.layout_for_custom_player_model.addWidget(self.custom_player_model)


        self.grid_for_model_general_options.addLayout(self.layout_for_custom_player_model, 0, 0, 1, 1)

        self.layout_for_custom_preset = QHBoxLayout()
        self.layout_for_custom_preset.setObjectName(u"layout_for_custom_preset")
        self.label_for_custom_color_preset = QLabel(self.tab_for_model_customization)
        self.label_for_custom_color_preset.setObjectName(u"label_for_custom_color_preset")

        self.layout_for_custom_preset.addWidget(self.label_for_custom_color_preset)

        self.custom_color_preset = QComboBox(self.tab_for_model_customization)
        self.custom_color_preset.setObjectName(u"custom_color_preset")

        self.layout_for_custom_preset.addWidget(self.custom_color_preset)


        self.grid_for_model_general_options.addLayout(self.layout_for_custom_preset, 1, 0, 1, 1)

        self.layout_for_sail_color = QHBoxLayout()
        self.layout_for_sail_color.setObjectName(u"layout_for_sail_color")
        self.label_for_sail_color = QLabel(self.tab_for_model_customization)
        self.label_for_sail_color.setObjectName(u"label_for_sail_color")

        self.layout_for_sail_color.addWidget(self.label_for_sail_color)

        self.sail_color = QComboBox(self.tab_for_model_customization)
        self.sail_color.addItem("")
        self.sail_color.addItem("")
        self.sail_color.addItem("")
        self.sail_color.setObjectName(u"sail_color")

        self.layout_for_sail_color.addWidget(self.sail_color)


        self.grid_for_model_general_options.addLayout(self.layout_for_sail_color, 3, 0, 1, 1)

        self.disable_custom_player_items = QCheckBox(self.tab_for_model_customization)
        self.disable_custom_player_items.setObjectName(u"disable_custom_player_items")

        self.grid_for_model_general_options.addWidget(self.disable_custom_player_items, 0, 2, 1, 1)

        self.disable_custom_player_voice = QCheckBox(self.tab_for_model_customization)
        self.disable_custom_player_voice.setObjectName(u"disable_custom_player_voice")

        self.grid_for_model_general_options.addWidget(self.disable_custom_player_voice, 1, 2, 1, 1)

        self.player_in_casual_clothes = QCheckBox(self.tab_for_model_customization)
        self.player_in_casual_clothes.setObjectName(u"player_in_casual_clothes")

        self.grid_for_model_general_options.addWidget(self.player_in_casual_clothes, 0, 1, 1, 1)

        self.layout_for_randomize_color_options = QHBoxLayout()
        self.layout_for_randomize_color_options.setObjectName(u"layout_for_randomize_color_options")
        self.randomize_all_custom_colors_together = QPushButton(self.tab_for_model_customization)
        self.randomize_all_custom_colors_together.setObjectName(u"randomize_all_custom_colors_together")

        self.layout_for_randomize_color_options.addWidget(self.randomize_all_custom_colors_together)

        self.randomize_all_custom_colors_separately = QPushButton(self.tab_for_model_customization)
        self.randomize_all_custom_colors_separately.setObjectName(u"randomize_all_custom_colors_separately")

        self.layout_for_randomize_color_options.addWidget(self.randomize_all_custom_colors_separately)


        self.grid_for_model_general_options.addLayout(self.layout_for_randomize_color_options, 2, 0, 1, 1)

        self.disable_custom_boat = QCheckBox(self.tab_for_model_customization)
        self.disable_custom_boat.setObjectName(u"disable_custom_boat")

        self.grid_for_model_general_options.addWidget(self.disable_custom_boat, 2, 2, 1, 1)

        self.custom_model_comment = QLabel(self.tab_for_model_customization)
        self.custom_model_comment.setObjectName(u"custom_model_comment")
        self.custom_model_comment.setMaximumSize(QSize(810, 16777215))
        self.custom_model_comment.setWordWrap(True)

        self.grid_for_model_general_options.addWidget(self.custom_model_comment, 1, 1, 2, 1)

        self.layout_for_custom_bck_entry = QHBoxLayout()
        self.layout_for_custom_bck_entry.setObjectName(u"layout_for_custom_bck_entry")
        self.label_for_custom_bck_entry = QLabel(self.tab_for_model_customization)
        self.label_for_custom_bck_entry.setObjectName(u"label_for_custom_bck_entry")
        self.label_for_custom_bck_entry.setEnabled(False)

        self.layout_for_custom_bck_entry.addWidget(self.label_for_custom_bck_entry)

        self.custom_bck_entry = QComboBox(self.tab_for_model_customization)
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.addItem("")
        self.custom_bck_entry.setObjectName(u"custom_bck_entry")
        self.custom_bck_entry.setEnabled(False)

        self.layout_for_custom_bck_entry.addWidget(self.custom_bck_entry)


        self.grid_for_model_general_options.addLayout(self.layout_for_custom_bck_entry, 3, 1, 1, 1)


        self.layout_for_customization.addLayout(self.grid_for_model_general_options)

        self.layout_for_color_visualizer = QHBoxLayout()
        self.layout_for_color_visualizer.setObjectName(u"layout_for_color_visualizer")
        self.layout_for_color_layout = QVBoxLayout()
        self.layout_for_color_layout.setObjectName(u"layout_for_color_layout")
        self.custom_colors_layout = QVBoxLayout()
        self.custom_colors_layout.setObjectName(u"custom_colors_layout")

        self.layout_for_color_layout.addLayout(self.custom_colors_layout)

        self.spacer_for_colors_layout = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_color_layout.addItem(self.spacer_for_colors_layout)


        self.layout_for_color_visualizer.addLayout(self.layout_for_color_layout)

        self.layout_for_model_preview = QVBoxLayout()
        self.layout_for_model_preview.setObjectName(u"layout_for_model_preview")
        self.custom_model_preview_label = QLabel(self.tab_for_model_customization)
        self.custom_model_preview_label.setObjectName(u"custom_model_preview_label")

        self.layout_for_model_preview.addWidget(self.custom_model_preview_label)

        self.spacer_for_model_preview = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_for_model_preview.addItem(self.spacer_for_model_preview)


        self.layout_for_color_visualizer.addLayout(self.layout_for_model_preview)


        self.layout_for_customization.addLayout(self.layout_for_color_visualizer)

        self.tab_for_main.addTab(self.tab_for_model_customization, "")

        self.layout_for_main_scroll.addWidget(self.tab_for_main)

        self.scroll_for_main.setWidget(self.content_for_main_scroll)

        self.vertical_layout_widget.addWidget(self.scroll_for_main)

        self.option_description = QLabel(self.centralwidget)
        self.option_description.setObjectName(u"option_description")
        self.option_description.setMinimumSize(QSize(0, 32))
        self.option_description.setWordWrap(True)

        self.vertical_layout_widget.addWidget(self.option_description)

        self.layout_for_permalink = QHBoxLayout()
        self.layout_for_permalink.setObjectName(u"layout_for_permalink")
        self.label_for_permalink = QLabel(self.centralwidget)
        self.label_for_permalink.setObjectName(u"label_for_permalink")

        self.layout_for_permalink.addWidget(self.label_for_permalink)

        self.permalink = QLineEdit(self.centralwidget)
        self.permalink.setObjectName(u"permalink")

        self.layout_for_permalink.addWidget(self.permalink)

        self.copy_button = QPushButton(self.centralwidget)
        self.copy_button.setObjectName(u"copy_button")

        self.layout_for_permalink.addWidget(self.copy_button)

        self.layout_for_permalink.setStretch(0, 1)
        self.layout_for_permalink.setStretch(1, 15)
        self.layout_for_permalink.setStretch(2, 2)

        self.vertical_layout_widget.addLayout(self.layout_for_permalink)

        self.update_checker_label = QLabel(self.centralwidget)
        self.update_checker_label.setObjectName(u"update_checker_label")
        self.update_checker_label.setOpenExternalLinks(True)

        self.vertical_layout_widget.addWidget(self.update_checker_label)

        self.layout_for_finalize = QHBoxLayout()
        self.layout_for_finalize.setObjectName(u"layout_for_finalize")
        self.about_button = QPushButton(self.centralwidget)
        self.about_button.setObjectName(u"about_button")

        self.layout_for_finalize.addWidget(self.about_button)

        self.horizontal_brake_for_about = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_finalize.addItem(self.horizontal_brake_for_about)

        self.reset_settings_to_default = QPushButton(self.centralwidget)
        self.reset_settings_to_default.setObjectName(u"reset_settings_to_default")
        self.reset_settings_to_default.setMinimumSize(QSize(180, 0))

        self.layout_for_finalize.addWidget(self.reset_settings_to_default)

        self.horizontal_brake_for_reset = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_for_finalize.addItem(self.horizontal_brake_for_reset)

        self.randomize_button = QPushButton(self.centralwidget)
        self.randomize_button.setObjectName(u"randomize_button")

        self.layout_for_finalize.addWidget(self.randomize_button)


        self.vertical_layout_widget.addLayout(self.layout_for_finalize)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_for_main.setCurrentIndex(0)
        self.logic_mod.setCurrentIndex(1)
        self.race_mode.setCurrentIndex(0)
        self.custom_bck_entry.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wind Waker Randomizer", None))
        self.label_for_clean.setText(QCoreApplication.translate("MainWindow", u"Clean WW ISO", None))
        self.label_for_output.setText(QCoreApplication.translate("MainWindow", u"Output Folder", None))
        self.output_folder_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_for_seed.setText(QCoreApplication.translate("MainWindow", u"Seed (optional)", None))
        self.generate_seed_button.setText(QCoreApplication.translate("MainWindow", u"New seed", None))
        self.clean_iso_path_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.logic_desc.setText("")
        self.label_for_logic_mod.setText(QCoreApplication.translate("MainWindow", u"Logic Type", None))
        self.logic_mod.setItemText(0, QCoreApplication.translate("MainWindow", u"Glitchless \u2013 Beginner", None))
        self.logic_mod.setItemText(1, QCoreApplication.translate("MainWindow", u"Glitchless \u2013 Standard", None))
        self.logic_mod.setItemText(2, QCoreApplication.translate("MainWindow", u"Glitched \u2013 Trivial", None))
        self.logic_mod.setItemText(3, QCoreApplication.translate("MainWindow", u"Glitched \u2013 Moderate", None))
        self.logic_mod.setItemText(4, QCoreApplication.translate("MainWindow", u"Glitched \u2013 Lunatic", None))
        self.logic_mod.setItemText(5, QCoreApplication.translate("MainWindow", u"Glitched \u2013 No Logic", None))

        self.logic_mod.setCurrentText(QCoreApplication.translate("MainWindow", u"Glitchless \u2013 Standard", None))
        self.group_for_locations.setTitle(QCoreApplication.translate("MainWindow", u"Where can progression be?", None))
        self.progression_island_puzzles.setText(QCoreApplication.translate("MainWindow", u"Island Puzzles", None))
        self.progression_long_combat_trials.setText(QCoreApplication.translate("MainWindow", u"Long Combat Trials", None))
        self.progression_mixed_secret_caves.setText(QCoreApplication.translate("MainWindow", u"Mixed Secret Caves", None))
        self.progression_combat_secret_caves.setText(QCoreApplication.translate("MainWindow", u"Combat Secret Caves", None))
        self.progression_tingle_chests.setText(QCoreApplication.translate("MainWindow", u"Odd Dungeon Checks", None))
        self.progression_big_octos_gunboats.setText(QCoreApplication.translate("MainWindow", u"Big Octos and Gunboats", None))
        self.progression_treasure_charts.setText(QCoreApplication.translate("MainWindow", u"Sunken Treasure (From Treasure Charts)", None))
        self.progression_submarines.setText(QCoreApplication.translate("MainWindow", u"Submarines", None))
        self.progression_platforms_rafts.setText(QCoreApplication.translate("MainWindow", u"Lookout Platforms and Rafts", None))
        self.progression_great_fairies.setText(QCoreApplication.translate("MainWindow", u"Great Fairies", None))
        self.progression_eye_reef_chests.setText(QCoreApplication.translate("MainWindow", u"Eye Reef Chests", None))
        self.progression_misc.setText(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.progression_puzzle_secret_caves.setText(QCoreApplication.translate("MainWindow", u"Puzzle Secret Caves", None))
        self.progression_spoils_trading.setText(QCoreApplication.translate("MainWindow", u"Spoils Trading", None))
        self.progression_triforce_charts.setText(QCoreApplication.translate("MainWindow", u"Sunken Treasure (From Triforce Charts)", None))
        self.progression_expensive_purchases.setText(QCoreApplication.translate("MainWindow", u"Expensive Purchases", None))
        self.progression_short_sidequests.setText(QCoreApplication.translate("MainWindow", u"Short Sidequests", None))
        self.progression_long_sidequests.setText(QCoreApplication.translate("MainWindow", u"Long Sidequests", None))
        self.progression_free_gifts.setText(QCoreApplication.translate("MainWindow", u"Free Gifts", None))
        self.progression_short_minigames.setText(QCoreApplication.translate("MainWindow", u"Short Minigames", None))
        self.progression_dungeons.setText(QCoreApplication.translate("MainWindow", u"Dungeons", None))
        self.progression_long_minigames.setText(QCoreApplication.translate("MainWindow", u"Long Minigames", None))
        self.group_for_settings_secondary.setTitle(QCoreApplication.translate("MainWindow", u"Dungeon Randomization Options", None))
        self.compass_map_pool_with_keys.setText(QCoreApplication.translate("MainWindow", u"Pool Dungeon Items with Keys", None))
        self.label_for_keymode.setText(QCoreApplication.translate("MainWindow", u"Key Placement", None))
        self.keymode.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.keymode.setItemText(1, QCoreApplication.translate("MainWindow", u"Cross Dungeon", None))
        self.keymode.setItemText(2, QCoreApplication.translate("MainWindow", u"Key-Lunacy", None))

        self.label_for_sword_mode.setText(QCoreApplication.translate("MainWindow", u"Sword Mode", None))
        self.sword_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Start with Hero's Sword", None))
        self.sword_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"No Starting Sword", None))
        self.sword_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Swordless", None))

        self.label_for_num_starting_triforce_shards.setText(QCoreApplication.translate("MainWindow", u"Starting Triforce Shards", None))
        self.num_starting_triforce_shards.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.num_starting_triforce_shards.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.num_starting_triforce_shards.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.num_starting_triforce_shards.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.num_starting_triforce_shards.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.num_starting_triforce_shards.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.num_starting_triforce_shards.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.num_starting_triforce_shards.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.num_starting_triforce_shards.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.num_starting_triforce_shards.setItemText(9, QCoreApplication.translate("MainWindow", u"Random", None))
        self.num_starting_triforce_shards.setItemText(10, QCoreApplication.translate("MainWindow", u"Mirror Dungeon Number", None))

        self.num_starting_triforce_shards.setCurrentText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_for_num_dungeon_race_mode.setText(QCoreApplication.translate("MainWindow", u"Number of Dungeons", None))
        self.num_dungeon_race_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.num_dungeon_race_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.num_dungeon_race_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.num_dungeon_race_mode.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.num_dungeon_race_mode.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.num_dungeon_race_mode.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.num_dungeon_race_mode.setItemText(6, QCoreApplication.translate("MainWindow", u"Random", None))

        self.num_dungeon_race_mode.setCurrentText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_for_race_mode.setText(QCoreApplication.translate("MainWindow", u"Dungeon Mode", None))
        self.race_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.race_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Mixed", None))
        self.race_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Race", None))

        self.add_shortcut_warps_between_dungeons.setText(QCoreApplication.translate("MainWindow", u"Add Shortcuts Between Dungeons", None))
        self.label_for_randomize_entrances.setText(QCoreApplication.translate("MainWindow", u"Randomize Entrances", None))
        self.randomize_entrances.setItemText(0, QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.randomize_entrances.setItemText(1, QCoreApplication.translate("MainWindow", u"Dungeons", None))
        self.randomize_entrances.setItemText(2, QCoreApplication.translate("MainWindow", u"Secret Caves", None))
        self.randomize_entrances.setItemText(3, QCoreApplication.translate("MainWindow", u"Dungeons & Secret Caves (Separately)", None))
        self.randomize_entrances.setItemText(4, QCoreApplication.translate("MainWindow", u"Dungeons & Secret Caves (Together)", None))

        self.group_for_convenience.setTitle(QCoreApplication.translate("MainWindow", u"Additional Options", None))
        self.label_for_can_chain_charts.setText(QCoreApplication.translate("MainWindow", u"Allow Charts in Sunken Treasure", None))
        self.can_chain_charts.setItemText(0, QCoreApplication.translate("MainWindow", u"Never", None))
        self.can_chain_charts.setItemText(1, QCoreApplication.translate("MainWindow", u"Sometimes", None))
        self.can_chain_charts.setItemText(2, QCoreApplication.translate("MainWindow", u"Always", None))

        self.reveal_full_sea_chart.setText(QCoreApplication.translate("MainWindow", u"Reveal Full Sea Chart", None))
        self.randomize_charts.setText(QCoreApplication.translate("MainWindow", u"Randomize Charts", None))
        self.randomize_starting_island.setText(QCoreApplication.translate("MainWindow", u"Randomize Starting Island", None))
        self.swift_sail.setText(QCoreApplication.translate("MainWindow", u"Use Swift Sail", None))
        self.instant_text_boxes.setText(QCoreApplication.translate("MainWindow", u"Instant Text Boxes", None))
        self.skip_rematch_bosses.setText(QCoreApplication.translate("MainWindow", u"Skip Boss Rematches", None))
        self.remove_title_and_ending_videos.setText(QCoreApplication.translate("MainWindow", u"Remove Title and Ending Videos", None))
        self.convenience_option_label.setText(QCoreApplication.translate("MainWindow", u"Item Pool", None))
        self.convenience_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.convenience_option.setItemText(1, QCoreApplication.translate("MainWindow", u"Convenient", None))
        self.convenience_option.setItemText(2, QCoreApplication.translate("MainWindow", u"Plentiful", None))
        self.convenience_option.setItemText(3, QCoreApplication.translate("MainWindow", u"Plentiful and Convenient", None))

        self.group_for_spoiler.setTitle(QCoreApplication.translate("MainWindow", u"Spoiler Options", None))
        self.generate_spoiler_log.setText(QCoreApplication.translate("MainWindow", u"Generate Spoiler Log", None))
        self.progression_check_spoiler_log.setText(QCoreApplication.translate("MainWindow", u"Include Playthrough", None))
        self.all_check_spoiler_log.setText(QCoreApplication.translate("MainWindow", u"Include All Check Locations", None))
        self.entrance_spoiler_log.setText(QCoreApplication.translate("MainWindow", u"Include Entrance Locations", None))
        self.chart_spoiler_log.setText(QCoreApplication.translate("MainWindow", u"Include Chart Locations", None))
        self.group_for_advanced.setTitle(QCoreApplication.translate("MainWindow", u"Advanced Options", None))
        self.invert_camera_x_axis.setText(QCoreApplication.translate("MainWindow", u"Invert Camera X-Axis", None))
        self.randomize_enemies.setText(QCoreApplication.translate("MainWindow", u"Randomize Enemy Locations", None))
        self.disable_tingle_chests_with_tingle_bombs.setText(QCoreApplication.translate("MainWindow", u"Tingle Bombs Don't Open Tingle Chests", None))
        self.randomize_enemy_palettes.setText(QCoreApplication.translate("MainWindow", u"Randomize Enemy Palettes", None))
        self.randomize_music.setText(QCoreApplication.translate("MainWindow", u"Randomize Music", None))
        self.remove_music.setText(QCoreApplication.translate("MainWindow", u"Remove Music", None))
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_settings), QCoreApplication.translate("MainWindow", u"Randomizer Settings", None))
        self.label_for_randomized_gear.setText(QCoreApplication.translate("MainWindow", u"Randomized Gear", None))
        self.remove_gear.setText(QCoreApplication.translate("MainWindow", u"🢀", None))
        self.add_gear.setText(QCoreApplication.translate("MainWindow", u"🢂", None))
        self.label_for_starting_gear.setText(QCoreApplication.translate("MainWindow", u"Starting Gear", None))
        self.label_for_additional_starting_min.setText(QCoreApplication.translate("MainWindow", u"Additional Starting Items: between", None))
        self.label_for_additional_starting_max.setText(QCoreApplication.translate("MainWindow", u"and", None))
        self.label_for_additional_starting.setText(QCoreApplication.translate("MainWindow", u"items.", None))
        self.text_for_total_starting_min.setText(QCoreApplication.translate("MainWindow", u"at least", None))
        self.label_for_total_starting.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.text_for_total_starting_max.setText(QCoreApplication.translate("MainWindow", u"starting items", None))
        self.label_for_starting_bh.setText(QCoreApplication.translate("MainWindow", u"Base Health", None))
        self.label_for_starting_hcs.setText(QCoreApplication.translate("MainWindow", u"Heart Containers", None))
        self.label_for_starting_pohs.setText(QCoreApplication.translate("MainWindow", u"Heart Pieces", None))
        self.current_health.setText(QCoreApplication.translate("MainWindow", u"Current Starting Health: 3 hearts", None))
        self.no_heart_in_pool.setText(QCoreApplication.translate("MainWindow", u"No Additional Health in Pool", None))
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_starting_items), QCoreApplication.translate("MainWindow", u"Starting Items", None))
        self.label_for_vanilla_entrances.setText(QCoreApplication.translate("MainWindow", u"Vanilla Entrances", None))
        self.add_vanilla_from_limited.setText(QCoreApplication.translate("MainWindow", u"🢀", None))
        self.add_limited_from_vanilla.setText(QCoreApplication.translate("MainWindow", u"🢂", None))
        self.add_vanilla_from_full.setText(QCoreApplication.translate("MainWindow", u"🢀", None))
        self.add_full_from_vanilla.setText(QCoreApplication.translate("MainWindow", u"🢂", None))
        self.label_for_limited_entrances.setText(QCoreApplication.translate("MainWindow", u"Randomized Limited-List Entrances", None))
        self.add_limited_from_full.setText(QCoreApplication.translate("MainWindow", u"🢁", None))
        self.add_full_from_limited.setText(QCoreApplication.translate("MainWindow", u"🢃", None))
        self.label_for_full_entrances.setText(QCoreApplication.translate("MainWindow", u"Randomized Full-List Entrances", None))
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_entrances), QCoreApplication.translate("MainWindow", u"Entrance Randomization", None))
        self.locale_stone_watcher.setText(QCoreApplication.translate("MainWindow", u"Stone Watcher", None))
        self.locale_dvim.setText(QCoreApplication.translate("MainWindow", u"dv_im checks", None))
        self.locale_six_eye.setText(QCoreApplication.translate("MainWindow", u"Six-Eye Reef", None))
        self.locale_picto.setText(QCoreApplication.translate("MainWindow", u"Picto Box", None))
        self.locale_southern_triangle.setText(QCoreApplication.translate("MainWindow", u"Southern Triangle", None))
        self.locale_bomb.setText(QCoreApplication.translate("MainWindow", u"Bomb Island", None))
        self.locale_ff.setText(QCoreApplication.translate("MainWindow", u"Forsaken Fortress", None))
        self.locale_five_eye.setText(QCoreApplication.translate("MainWindow", u"Five-Eye Reef", None))
        self.locale_boating_course.setText(QCoreApplication.translate("MainWindow", u"Boating Course", None))
        self.locale_spectacle.setText(QCoreApplication.translate("MainWindow", u"Spectacle Island", None))
        self.locale_forest_haven.setText(QCoreApplication.translate("MainWindow", u"Forest Haven", None))
        self.locale_angular.setText(QCoreApplication.translate("MainWindow", u"Angular Isles", None))
        self.locale_seven_star.setText(QCoreApplication.translate("MainWindow", u"Seven-Star Isles", None))
        self.locale_eastern_fairy.setText(QCoreApplication.translate("MainWindow", u"Eastern Fairy", None))
        self.locale_four_eye.setText(QCoreApplication.translate("MainWindow", u"Four-Eye Reef", None))
        self.locale_star.setText(QCoreApplication.translate("MainWindow", u"Star Island", None))
        self.locale_tingle.setText(QCoreApplication.translate("MainWindow", u"Tingle Island", None))
        self.locale_crescent.setText(QCoreApplication.translate("MainWindow", u"Crescent Moon", None))
        self.locale_western_fairy.setText(QCoreApplication.translate("MainWindow", u"Western Fairy", None))
        self.locale_shark.setText(QCoreApplication.translate("MainWindow", u"Shark Island", None))
        self.locale_gale.setText(QCoreApplication.translate("MainWindow", u"Gale Isle", None))
        self.locale_fire_mountain.setText(QCoreApplication.translate("MainWindow", u"Fire Mountain", None))
        self.locale_private_oasis.setText(QCoreApplication.translate("MainWindow", u"Private Oasis", None))
        self.locale_overlook.setText(QCoreApplication.translate("MainWindow", u"Overlook Island", None))
        self.locale_greatfish.setText(QCoreApplication.translate("MainWindow", u"Greathfish Isle", None))
        self.locale_northern_triangle.setText(QCoreApplication.translate("MainWindow", u"Northern Triangle", None))
        self.locale_two_eye.setText(QCoreApplication.translate("MainWindow", u"Two-Eye Reef", None))
        self.locale_five_star.setText(QCoreApplication.translate("MainWindow", u"Five-Star Isles", None))
        self.locale_savage.setText(QCoreApplication.translate("MainWindow", u"Savage Labyrinth", None))
        self.locale_rock_spire.setText(QCoreApplication.translate("MainWindow", u"Rock Spire Isle", None))
        self.locale_star_belt.setText(QCoreApplication.translate("MainWindow", u"Star Belt", None))
        self.locale_dragon_roost_island.setText(QCoreApplication.translate("MainWindow", u"Dragon Roost", None))
        self.locale_mother_child.setText(QCoreApplication.translate("MainWindow", u"Mother and Child", None))
        self.locale_windfall.setText(QCoreApplication.translate("MainWindow", u"Windfall Island", None))
        self.locale_pawprint.setText(QCoreApplication.translate("MainWindow", u"Pawprint Isle", None))
        self.locale_ice_ring.setText(QCoreApplication.translate("MainWindow", u"Ice Ring Isle", None))
        self.locale_birds_peak.setText(QCoreApplication.translate("MainWindow", u"Bird's Peak Rock", None))
        self.locale_flight_control.setText(QCoreApplication.translate("MainWindow", u"Flight Control", None))
        self.locale_cyclops.setText(QCoreApplication.translate("MainWindow", u"Cyclops Reef", None))
        self.locale_southern_fairy.setText(QCoreApplication.translate("MainWindow", u"Southern Fairy", None))
        self.locale_headstone.setText(QCoreApplication.translate("MainWindow", u"Headstone Island", None))
        self.locale_eastern_triangle.setText(QCoreApplication.translate("MainWindow", u"Eastern Triangle", None))
        self.locale_outset.setText(QCoreApplication.translate("MainWindow", u"Outset Island", None))
        self.locale_thorned_fairy.setText(QCoreApplication.translate("MainWindow", u"Thorned Fairy", None))
        self.locale_northern_fairy.setText(QCoreApplication.translate("MainWindow", u"Northern Fairy", None))
        self.locale_islet.setText(QCoreApplication.translate("MainWindow", u"Islet of Steel", None))
        self.locale_three_eye.setText(QCoreApplication.translate("MainWindow", u"Three-Eye Reef", None))
        self.locale_cliff_plateau.setText(QCoreApplication.translate("MainWindow", u"Cliff Plateau Isles", None))
        self.locale_mail.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.locale_needle_rock.setText(QCoreApplication.translate("MainWindow", u"Needle Rock Isle", None))
        self.locale_horseshoe.setText(QCoreApplication.translate("MainWindow", u"Horseshoe Island", None))
        self.locale_diamond_steppe.setText(QCoreApplication.translate("MainWindow", u"Diamond Steppe", None))
        self.locale_battlesquid.setText(QCoreApplication.translate("MainWindow", u"Battlequids", None))
        self.locale_deep_et.setText(QCoreApplication.translate("MainWindow", u"Deep ET", None))
        self.locale_et.setText(QCoreApplication.translate("MainWindow", u"ET", None))
        self.locale_wt.setText(QCoreApplication.translate("MainWindow", u"WT", None))
        self.locale_drc.setText(QCoreApplication.translate("MainWindow", u"DRC", None))
        self.locale_totg.setText(QCoreApplication.translate("MainWindow", u"TotG", None))
        self.locale_fw.setText(QCoreApplication.translate("MainWindow", u"FW", None))
        self.locale_under_great_sea.setText(QCoreApplication.translate("MainWindow", u"Under Great Sea", None))
        self.locale_great_sea.setText(QCoreApplication.translate("MainWindow", u"Great Sea", None))
        self.locale_deep_drc.setText(QCoreApplication.translate("MainWindow", u"Deep DRC", None))
        self.locale_deep_fw.setText(QCoreApplication.translate("MainWindow", u"Deep FW", None))
        self.locale_deep_totg.setText(QCoreApplication.translate("MainWindow", u"Deep TotG", None))
        self.locale_deep_wt.setText(QCoreApplication.translate("MainWindow", u"Deep WT", None))
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_locales), QCoreApplication.translate("MainWindow", u"Banned Locales", None))
        self.label_for_custom_player_model.setText(QCoreApplication.translate("MainWindow", u"Player Model", None))
        self.label_for_custom_color_preset.setText(QCoreApplication.translate("MainWindow", u"Color Preset", None))
        self.label_for_sail_color.setText(QCoreApplication.translate("MainWindow", u"Sail", None))
        self.sail_color.setItemText(0, QCoreApplication.translate("MainWindow", u"Sail of Red Lions", None))
        self.sail_color.setItemText(1, QCoreApplication.translate("MainWindow", u"Swift Sail", None))
        self.sail_color.setItemText(2, QCoreApplication.translate("MainWindow", u"Sail of Lions' Pride", None))

        self.disable_custom_player_items.setText(QCoreApplication.translate("MainWindow", u"Disable Custom Items", None))
        self.disable_custom_player_voice.setText(QCoreApplication.translate("MainWindow", u"Disable Custom Voice", None))
        self.player_in_casual_clothes.setText(QCoreApplication.translate("MainWindow", u"Casual Clothes", None))
        self.randomize_all_custom_colors_together.setText(QCoreApplication.translate("MainWindow", u"Randomize Colors Orderly", None))
        self.randomize_all_custom_colors_separately.setText(QCoreApplication.translate("MainWindow", u"Randomize Colors Chaotically", None))
        self.disable_custom_boat.setText(QCoreApplication.translate("MainWindow", u"Disable Custom Boat", None))
        self.custom_model_comment.setText("")
        self.label_for_custom_bck_entry.setText(QCoreApplication.translate("MainWindow", u"Animation Deviation", None))
        self.custom_bck_entry.setItemText(0, QCoreApplication.translate("MainWindow", u"No Changes", None))
        self.custom_bck_entry.setItemText(1, QCoreApplication.translate("MainWindow", u"Not Gameplay", None))
        self.custom_bck_entry.setItemText(2, QCoreApplication.translate("MainWindow", u"Basic Gameplay", None))
        self.custom_bck_entry.setItemText(3, QCoreApplication.translate("MainWindow", u"All", None))

        self.custom_model_preview_label.setText("")
        self.tab_for_main.setTabText(self.tab_for_main.indexOf(self.tab_for_model_customization), QCoreApplication.translate("MainWindow", u"Player Customization", None))
        self.option_description.setText("")
        self.label_for_permalink.setText(QCoreApplication.translate("MainWindow", u"Permalink:", None))
        self.copy_button.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.update_checker_label.setText(QCoreApplication.translate("MainWindow", u"Checking for updates to the randomizer...", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.reset_settings_to_default.setText(QCoreApplication.translate("MainWindow", u"Reset All Settings to Default", None))
        self.randomize_button.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
    # retranslateUi
