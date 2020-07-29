### ModelData ###
    name : specimen 이름 ex) RP01
    crv_name : specimen 이름에 분석할 근관의 약자를 붙임 ex)RP01-B
    cnl_ref<Canal> :
    **cnls_cmp{name:<Canal>} : optional
    crv_ref_length
    evaluating_canal_furcation
    facets_cnl_ref
    **facets_cnls_cmp{}
    furcatoin_pos_buccal
    furcatoin_pos_lingual
    length_buccal
    length_lingual
    median_major_axis_vector
    pts_of_crv_opp_ref
    pts_of_crv_ref
    **pts_of_crvs_cmp
    tooth_position
    specimen<Specimen> : 치근과 근관의 정보 관리
        name : 시편의 이름
        tooth_position : UpperRight, UpperLeft, LowerRight, LowerLeft //UR, UL, LR, LL = 0, 1, 2, 3
        body_path : path to v3d file (치근 외형)
        bounding_box : coordiantion
        canal_type : 별 의미 없음
        note : 특이사항
        canals<Canal>[]
            Canal :
                name
                path : path to v3d file
                furcation_pos_buccal
                furcation_pos_lingual
                pts_buccal : v-works에서 canal center plotting coordination
                pts_lingual : v-works에서 canal center plotting coordination
                curve_buccal<Nerve_path> :pts_buccal 정보를 이용해서 만든 spline curve
                curve_lingual<Nerve_path> : pts_lingual 정보를 이용해서 만든 spline curve
                length_buccal
                length_lingual



