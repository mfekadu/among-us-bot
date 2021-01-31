import tasks

tasks_loc = [
    ["Align Engine (Upper Engine)", (273, 355), tasks.align_engine_output],  #
    ["Align Engine (Lower Engine)", (275, 854), tasks.align_engine_output],  #
    ["Calibrate Distributor", (817, 643), tasks.calibrate_distributor],  #
    ["Chart Course", (1796, 432), tasks.chart_course],  #
    ["Clean O2 Filter", (1293, 460), tasks.clean_O2_filter],  #
    ["Clear Asteroids", (1430, 262), tasks.clear_asteroids],  #
    ["Divert Power", (690, 635), tasks.divert_power],  #
    ["Accept Power (Communications)", (1310, 914), tasks.accept_power],  #
    ["Accept Power (Lower Engine)", (322, 717), tasks.accept_power],  #
    ["Accept Power (Upper Engine)", (352, 209), tasks.accept_power],  #
    ["Accept Power (Navigation)", (1712, 437), tasks.accept_power],  #
    ["Accept Power (O2)", (1400, 441), tasks.accept_power],  #
    ["Accept Power (Security)", (562, 462), tasks.accept_power],  #
    ["Accept Power (Shields)", (1496, 763), tasks.accept_power],  #
    ["Accept Power (Weapons)", (1525, 252), tasks.accept_power],  #
    ["Empty Garbage/Chute (Cafeteria)", (1241, 176), tasks.empty_chute],  #
    ["Empty Garbage/Chute (O2)", (1260, 473), tasks.empty_chute],  #
    ["Empty Garbage/Chute (Storage)", (1092, 1020), tasks.empty_chute],  #
    ["Fix Wires (Electrical)", (742, 651), tasks.fix_wires],  #
    ["Fix Wires (Storage)", (978, 696), tasks.fix_wires],  #
    ["Fix Wires (Security)", (422, 528), tasks.fix_wires],  #
    ["Fix Wires (Navigation)", (1652, 492), tasks.fix_wires],
    ["Fix Wires (Admin)", (1114, 599), tasks.fix_wires],  #
    ["Fix Wires (Cafeteria)", (841, 124), tasks.fix_wires],  #
    ["Fuel Engine (Storage)", (941, 906), tasks.fuel_engines],  #
    ["Fuel Engine (Lower Engine)", (308, 852), tasks.fuel_engines],  #
    ["Fuel Engine (Upper Engine)", (308, 350), tasks.fuel_engines],  #
    ["Inspect Sample", (808, 513), tasks.inspect_sample],  #
    ["Prime Shields", (1367, 910), tasks.prime_shields],  #
    ["Stabilize Steering", (1824, 532), tasks.stabilize_steering],  #
    ["Start Reactor", (166, 565), tasks.start_reactor],  #
    ["Submit Scan", (757, 552), tasks.submit_scan],  #
    ["Swipe Card", (1289, 691), tasks.swipe_card],  # Changed
    ["Unlock Manifolds", (135, 440), tasks.unlock_manifold],  #
    ["Download/Upload (Cafeteria)", (1200, 137), tasks.download_upload],  #
    ["Download/Upload (Admin)", (1160, 593), tasks.download_upload],  #
    ["Download/Upload (Communications)", (1215, 908), tasks.download_upload],  # changed
    ["Download/Upload (Electrical)", (655, 585), tasks.download_upload],  #
    ["Download/Upload (Navigation)", (1752, 438), tasks.download_upload],  #
    ["Download/Upload (Weapons)", (1413, 177), tasks.download_upload],
]  #
