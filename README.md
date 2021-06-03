# README #

last updated 2018.07.16

### What is this repository for? ###

* Quick summary

1. Read v3d model
2. analysis each sliced sections
3. export the results to JSON file or Excel file

* Running the application
1. v3d model준비
    1. v3d model directory 를 별도로 준비해야함
    2. 시스템 환경변수 'TOOTH_DATA'를 v3d model directory로 설정(ex D:\Dropbox\11.mct.section.analysis\v3d.models)

1. analysis directory의 class_model_data또는 class_section_data의 main()을 실행


### Directory description ###
1. analysis : main directory
    1. class_model_data : 
        1. 하나의 치아모델(치근외형 1개, 근관외형 복수개), 근관 중심축의 좌표 등의 정보를 가진 class
        2. 모델의 정보는 v3d_model_info directory 에서 읽음
    2. class_section_data :
        1. class_model_data의 instance를 이용, 모델을 사용자 정의 간격으로 section을 만들어 각각을 분석함
        2. 분석한 정보는 dictionary 형식으로 JOSN파일로 저장
    3. data_analyzer :
        1. class_section_data에서 저장한 JSON 파일을 읽은후 필요한 정보를 excel로 저장
2. shared : main module에서 사용하는 helper module들이 정의됨
3. toothlab_exports :class_section_data 의 instance 를 생성해서 toothlab에서 사용할 정보들을 만듦
4. results : 분석결과를 출력하는 directory
          
    
### Kappa2 install (python 3.8.2)
activate py38
pip install pandas
conda install shapely
pip install numpy-stl
conda install -c anaconda pywin32
pip install streamlit
pip install plotly
pip install matplotlib
pip install openpyxy
pip install pyvista
--conda install -c conda-forge opencv
    

### Kappa2 installation ###

    Anaconda 2.7 32 bit version install
    (nerve_path가 32 python 32 bit application임)
    
    
    shapely install
    @@ anaconda prompt(관리자 권한으로 실행)
    >> conda install -c scitools/label/archive shapely
    
    pywin32 install
    >> conda install -c anaconda pywin32
    
    http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win32-py2.7.exe/download
    
    openCV install
    anaconda cv2 install 검색


### 3D model preparation ###

A. v3d to wrl files

    run export_wrls() module in class_model_data.py
    It exports all v3d files to corresponding wrl files

B. wrl to x3d files

    use MeshLab software
    1. load wrl files and apply filters
      [Filters]->[Remeshing, Simplication and reconstruction]
        ->Simplacation:Clustering Decimation
        options : cell size, [0.1] world unit
    2. [Export Mesh As..] 에서 x3d file로 저장

C. Canal Axis preparation

* use Openscad software
    


### 마이크로 CT 촬영 프로토콜 ###

* 치아의 준비

    1. 치아에 묻은 이물질 모두 제거(스케일러로)
    2. 관찰하고자 하는 부위는 치아 상태 그대로여야함(이물질 붙이지 말것).
    3. 만일 방향을 표시하려고 치아표면에 표식을 붙인다면 크라운 부위에 아주 작은 크기로
    4. 치근의 일부를 삭제한다면 관찰하려는 부분은 손상되지 않도록  깔끔하게 삭제할것


* 촬영


    1. 촬영시 치아의 축이 가로 또는 세로가 되도록 위치시킴
    (사선이 되면 이미지 영역이 커지고 컴퓨터로 이미지 처리하는 데 한계가 있음)

    +---------------------------------------------+
    |         *****            *******            |
    |     *            ********           **      |
    |   *                                      *  |
    |    *         **********              *      |
    |       *****                 ********        |
    +---------------------------------------------+

## module nerve_path

    class Nerve_path : python 2.7로 compile 됨
    static create(points)
        points를 interpolation하는 오더 3의 B-spline을 나타내는 Nerve_path를 만든다.
    get_appr_len()
    get_pos(u)
        매개 변수 u에 해당하는 점을 돌려준다. (0 ? u ? 1)
    get_diff1(u)
        매개 변수 u에 해당하는 점에서의 1차 미분값을 돌려준다. (0 ? u ? 1)
    get_curvature(l)
        (curve의 길이)?l에 해당하는 점에서의 curvature을 돌려준다. (0 ? l ? 1)
    get_torsion(l)
        (curve의 길이)?l에 해당하는 점에서의 torsion을 돌려준다. (0 ? l ? 1)
    length_to_parameter(l)
        (curve의 길이)?l에 해당하는 점에 대응하는 매개변수 u를 돌려준다. (0 ? l ? 1)
    parameter_to_length (u)
        매개변수 u에 해당하는 점에 대응하는 l을 돌려준다. (0 ? l ? 1)

