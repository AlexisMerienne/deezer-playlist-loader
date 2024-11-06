def test_duplicated_tracks():

    tracks = ['2732617791', '2511970', '2454854755', '2742341611', '579893072', '2614309112', '2481410771', '2857442072', '2953227', '2010886827', '2690049952', '2112339', '2758952051', '2480947801', '2684849612', '3501645', '2734749731', '2572172782', '2715036742', '2368732225', '2774027681', '2502700551', '2851591152', '86453301', '2729774671', '2755140501', '2851370612', '1343064662', '2874893852', '2738083021', '2834151182', '2803123092', '2775062681', '2482037931', '2816363462', '2757496011', '876197002', '2857029802', '2450838215', '2642284962', '63534466', '2537957421', '2832495592', '658106772', '2679206532', '2843874352', '2742341611', '2742721201', '2893833581', '2456838515', '2743570371', '2728950121', '1449740502', '2867128102', '2851339202', '2617445192', '2857442072', '2741217521', '830336932', '1442723522', '2893144961', '2761976311', '2349077615', '2454854755', '2732617791', '115705672', '2805848732', '2701335722', '2851591152', '872421772', '2481456361', '2642715092', '2684849612', '1090761132', '2672689962', '2817709702', '2803123092', '1091037332', '2521476601', '2755140501', '17347967', '2893102941', '1842063487', '2742721171', '2816363462', '2758952051', '1459923222', '2690049952', '1964235857', '2874893852', '2734749731', '2480947801', '2715036742', '13783454', '2502700551', '2742721151', '2893833581', '140861955', '2775062681', '2572172782', '962518', '2315939975', '2857029802', '2742341611', '13208968', '2106871457', '2738083021', '1071305612', '2857442072', '2877072562', '2269127797', '536935', '2834151182', '2732617791', '2537957421', '2893833601', '2094783217', '2803123092', '2729774671', '1043576', '2679206532', '2286113817', '2642284962', '2755140501', '2728950121', '2482037931', '2867128102', '568003', '2851370612', '2617445192', '100422966', '2287945487', '2893144961', '2741217521', '2816363462', '1104084772', '2703802792', '2874893902', '2684849612', '925111', '2761976311', '2832495592', '2742721201', '2166050087', '1463286702', '2743570371', '2893102941', '90265813', '2843874352', '2452283375', '2893833581', '2614309112', '13783453', '2805848732', '2666457402', '2690049952', '1459896832', '2481456361', '2742721151', '2874893852', '69982615', '2454854755', '2851591152', '870979432', '2454014645', '2642715092', '2758952051', '2715036742', '564946502', '2149221017', '2817709702', '2742341611', '2803123092',
              '2486051731', '580936', '2757496011', '2857442072', '2734749731', '459488622', '2774027681', '2296960375', '2867128102', '139102925', '2502700551', '2055292027', '2315939975', '143169092', '2775062681', '2701335722', '2732617791', '438748602', '2857029802', '2755140501', '629899852', '2572172782', '2537957421', '2684849612', '121219132', '2387373015', '2738083021', '2893833581', '1387503942', '2874893852', '585507822', '2834151182', '2832495592', '2679206532', '89735107', '2877072562', '2684849712', '2851591152', '2729774671', '2741217521', '2020394177', '2893833601', '2893102941', '3822645', '2851370612', '2851339202', '2761976311', '1442723522', '1761135797', '2482037931', '2805848732', '2742341611', '2471145121', '2867128102', '2481456361', '2715036742', '2642284962', '2127476587', '66190255', '2743570371', '2803123092', '2742721201', '1962187307', '2614309112', '4708756', '2728950121', '2732553231', '2874893902', '2816363462', '845095592', '2480947801', '2893833581', '2511975', '2758952051', '2454854755', '2755140501', '2410501775', '2617445192', '2734749731', '2857442072', '141826655', '2631254442', '2642715092', '2851591152', '83945015', '2893102941', '2843874352', '2149221037', '6917807', '2893144961', '2775062681', '5420471', '2774027681', '2874893852', '611666082', '2857029802', '2433420955', '2742721171', '2742341611', '2279314817', '2537957421', '2315939975', '2832495592', '823567772', '2742721151', '2867128102', '15475926', '2701335722', '2679206532', '2816363462', '2817709702', '2755140501', '869547', '2741217521', '1558993432', '1959441337', '2738083021', '2761976311', '2729774671', '2201843247', '2893833581', '2690049952', '2805848732', '2269127857', '2851339202', '2893102941', '15590961', '2481456361', '2572172782', '2684849612', '1075781', '2877072562', '2732617791', '477452252', '2182389237', '2482037931', '2715036742', '1459907052', '2233803177', '1125953', '2851370612', '2851591152', '2285516547', '2793681', '2614309112', '2857442072', '2758952051', '2617445192', '2803123092', '2757496011', '2874893902', '2742341611', '1161678', '2734749731', '2834151182', '2867128102', '2502700551', '2774027681', '2816363462', '644296792', '2480947801', '2775062681', '2755140501', '967328', '2454854755', '2893833581', '772257', '2874893852', '2642284962', '2286113817', '62082980', '2743570371', '2832495592', '2857029802']
    print(len(tracks))
    tracks = set(tracks)
    print(len(tracks))


if __name__ == '__main__':
    test_duplicated_tracks()
