import csv
import pandas as pd 
import numpy as np

def cut_sections(list_information: list, headers: set, section_name: str) -> list:
    """Documentation
    INPUT : list_information(list) -> la informacion del csv en formato de lista
    OUTPUT : gatherer(list) -> lista donde cada elemente 
    """

    # Cada elemento en gatherer es una seccion
    gatherer = []
    # Section se encargara de llenarse con la informacion de cada seccion
    section = []
    counter = 0
    try:
        print(f'##########SECCION : {section_name}##########')
        for row in list_information:
            if len(row) > 0 and row[0] in headers:
                counter = counter + 1
                print(f'Seccion :{row[0]} encontrada {counter} de {len(headers)}')
                if len(section) > 0:
                    gatherer.append(section)
                    section = []
                    section.append(row)
                else:
                    section.append(row)
            else:
                section.append(row)
        gatherer.append(section)
        return gatherer
    except:
        return 'Ocurrio un problema con la funcion cut_sections'

''' Funciones
'''
def ipr_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2](list) -> Lista con los dataframes
    ---
    """
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1 -> ['PI', 'FBHP']
    [2] = df2 -> ['Flowrate', 'Pressure']
    """
    try:
        # Filtrando los titulos de la lista
        header_1 = data[1][:2]
        header_2 = data[1][2:]

        # Filtrando los datos para sus respectivos titulos
        data_1 = np.array(data[2])
        data_2 = [row[2:] for row in data[3:] if len(row) > 0]

        # Transformando los string a flotante
        data_2 = [[float(x[0]), float(x[1])] for x in data_2]
        data_2 = np.array(data_2)

        # Formando los dataframes
        df1 = pd.DataFrame(columns=header_1, data=[data_1])
        df2 = pd.DataFrame(columns=header_2, data=data_2)

        return [doc, df1, df2]
    except:
        return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def z_plot_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1](list) -> Lista con un dataframe
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1 -> ['Depth', 'Pressure']
    """
    try:
        # Filtrando el titulo
        header_1 = data[1]

        # Filtrando los datos: recorre todas las filas hasta  que una fila este vacia
        data_1 = []
        for row in data[2:]:
            if len(row) > 0 :
                data_1.append(row)
            else:
                break

        # Transformando los string a flotante
        data_1 = [[float(x[0]), float(x[1])] for x in data_1]
        data_1 = np.array(data_1)

        # Formando los dataframes
        df1 = pd.DataFrame(columns=header_1, data=data_1)

        return [doc, df1]
    except:
        return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto z_plot_Data'

def vfd_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2, df3, df4](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(IPRCURVE) -> ['Flowrate', 'Pressure']
    [2] = df2(45hz) -> ['Flowrate', 'Pressure']
    [3] = df3(50hz) -> ['Flowrate', 'Pressure']
    [4] = df4(55hz) -> ['Flowrate', 'Pressure']
    """
    #     try:
    sections = {'IPRCurve', '45Hz', '50Hz', '55Hz'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'VFDData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = cuted_sections[1][1]
    header_3 = cuted_sections[2][1]
    header_4 = cuted_sections[3][1]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break        
    data_2 = [] # 45hz
    for row in cuted_sections[1][2:]:
        if len(row) > 0 :
            data_2.append(row)
        else:
            break                    
    data_3 = []
    for row in cuted_sections[2][2:]:
        if len(row) > 0 :
            data_3.append(row)
        else:
            break
    data_4 = []
    for row in cuted_sections[3][2:]:
        if len(row) > 0 :
            data_4.append(row)
        else:
            break

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1])] for x in data_1]
    data_2 = [[float(x[0]), float(x[1])] for x in data_2]
    data_3 = [[float(x[0]), float(x[1])] for x in data_3]
    data_4 = [[float(x[0]), float(x[1])] for x in data_4] 

    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=data_2)
    df3 = pd.DataFrame(columns=header_3, data=data_3)
    df4 = pd.DataFrame(columns=header_4, data=data_4)

    return [doc, df1, df2, df3, df4]

def base_pump_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(BasePumpCurveData) -> ['flowrate', 'BHPCurve', 'EfficiencyCurve', 'HeadFTCurve', 'HeadPsiCurve']
    [2] = df2 -> ['MinROR', 'MaxROR', 'BEP']
    """
    #     try:
    sections = {'BasePumpCurveData', 'MinROR', 'MaxROR', 'BEP'}

    cuted_sections = cut_sections(data, sections, 'BasePumpCurveData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = [cuted_sections[1][0][0], cuted_sections[2][0][0], cuted_sections[3][0][0]]
    
    # Filtrando los datos para sus respectivos titulos
    # cuted_sections[0][2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break

    # Formando un solo dataframe para Minror Maxror y Bep
    data_2 = [float(cuted_sections[1][1][0]), float(cuted_sections[2][1][0]), float(cuted_sections[3][1][0])] 

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=[data_2])

    return [doc, df1, df2]

def operating_freq_pump_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(BasePumpCurveData) -> ['flowrate', 'BHPCurve', 'EfficiencyCurve', 'HeadFTCurve', 'HeadPsiCurve']
    [2] = df2 -> ['MinROR', 'MaxROR', 'BEP']
    """
    #     try:
    sections = {'OperatingFrequencyPumpCurveData', 'MinROR', 'MaxROR', 'BEP'}

    cuted_sections = cut_sections(data, sections, 'OperatingFrequencyPumpCurveData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = [cuted_sections[1][0][0], cuted_sections[2][0][0], cuted_sections[3][0][0]]

    # Filtrando los datos para sus respectivos titulos
    # cuted_sections[0][2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break

    # Formando un solo dataframe para Minror Maxror y Bep
    data_2 = [float(cuted_sections[1][1][0]), float(cuted_sections[2][1][0]), float(cuted_sections[3][1][0])] 

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=[data_2])

    return [doc, df1, df2]

def derated_operating_freq_pump_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(BasePumpCurveData) -> ['flowrate', 'BHPCurve', 'EfficiencyCurve', 'HeadFTCurve', 'HeadPsiCurve']
    [2] = df2 -> ['MinROR', 'MaxROR', 'BEP']
    """
    #     try:
    sections = {'DeratedOperatingFrequencyPumpCurveData', 'MinROR', 'MaxROR', 'BEP'}

    cuted_sections = cut_sections(data, sections, 'DeratedOperatingFrequencyPumpCurveData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = [cuted_sections[1][0][0], cuted_sections[2][0][0], cuted_sections[3][0][0]]

    # Filtrando los datos para sus respectivos titulos
    # cuted_sections[0][2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break

    # Formando un solo dataframe para Minror Maxror y Bep
    data_2 = [float(cuted_sections[1][1][0]), float(cuted_sections[2][1][0]), float(cuted_sections[3][1][0])] 

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=[data_2])

    return [doc, df1, df2]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def operating_freq_insitu_pump_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(BasePumpCurveData) -> ['flowrate', 'BHPCurve', 'EfficiencyCurve', 'HeadFTCurve', 'HeadPsiCurve']
    [2] = df2 -> ['MinROR', 'MaxROR', 'BEP']
    """
    #     try:
    sections = {'OperatingFrequencyInsituPumpCurveData', 'MinROR', 'MaxROR', 'BEP'}

    cuted_sections = cut_sections(data, sections, 'OperatingFrequencyInsituPumpCurveData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = [cuted_sections[1][0][0], cuted_sections[2][0][0], cuted_sections[3][0][0]]

    # Filtrando los datos para sus respectivos titulos
    # cuted_sections[0][2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break

    # Formando un solo dataframe para Minror Maxror y Bep
    data_2 = [float(cuted_sections[1][1][0]), float(cuted_sections[2][1][0]), float(cuted_sections[3][1][0])] 

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=[data_2])

    return [doc, df1, df2]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def derated_operating_freq_insitu_pump_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(BasePumpCurveData) -> ['flowrate', 'BHPCurve', 'EfficiencyCurve', 'HeadFTCurve', 'HeadPsiCurve']
    [2] = df2 -> ['MinROR', 'MaxROR', 'BEP']
    """
    #     try:
    sections = {'DeratedOperatingFrequencyInsituPumpCurveData', 'MinROR', 'MaxROR', 'BEP'}

    cuted_sections = cut_sections(data, sections, 'DeratedOperatingFrequencyInsituPumpCurveData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = [cuted_sections[1][0][0], cuted_sections[2][0][0], cuted_sections[3][0][0]]

    # Filtrando los datos para sus respectivos titulos
    # cuted_sections[0][2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break

    # Formando un solo dataframe para Minror Maxror y Bep
    data_2 = [float(cuted_sections[1][1][0]), float(cuted_sections[2][1][0]), float(cuted_sections[3][1][0])] 

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=[data_2])

    return [doc, df1, df2]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def operating_point_analysis_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2, df3, df4, df5](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(PumpCurves) -> ['flowrate', 'BHPCurve', 'EfficiencyCurve', 'HeadCurve']
    [2] = df2(WellCurve) -> ['flowrate', 'FBHP']
    [3] = df3() -> ['BepRate', 'MinROR', 'MaxROR']
    [4] = df4(OperatingPointData) -> ['FlowRate', 'Pressure']
    [5] = df5(ThrustStatus) -> ['ThrustStatus']
    """
    #     try:
    sections = {'PumpCurves', 'WellCurve', 'BepRate', 'OperatingPointData', 'ThrustStatus'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'OperatingPointAnalysisData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = cuted_sections[1][1]
    header_3 = cuted_sections[2][0]
    header_4 = cuted_sections[3][1]
    header_5 = cuted_sections[4][0]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = [] # IPRCURVE
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break        
    data_2 = [] # 45hz
    for row in cuted_sections[1][2:]:
        if len(row) > 0 :
            data_2.append(row)
        else:
            break                    
    data_3 = cuted_sections[2][1]
                                  
    data_4 = cuted_sections[3][2]
                                  
    data_5 = cuted_sections[4][1]

    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1]), float(x[2]), float(x[3])] for x in data_1]
    data_2 = [[float(x[0]), float(x[1])] for x in data_2]
    data_3 = [float(data_3[0]), float(data_3[1]), float(data_3[2])]
    data_4 = [float(data_4[0]), float(data_4[1])]

    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=data_2)
    df3 = pd.DataFrame(columns=header_3, data=[data_3])
    df4 = pd.DataFrame(columns=header_4, data=[data_4])
    df5 = pd.DataFrame(columns=header_5, data=[data_5])

    return [doc, df1, df2, df3, df4, df5]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def funnel_curves(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(40Hz) -> ['Flowrate', 'Head']
    [2] = df2(50hz) -> ['Flowrate', 'Head']
    [3] = df3(60hz) -> ['Flowrate', 'Head']
    [4] = df4(70hz) -> ['Flowrate', 'Head']
    [5] = df5(80Hz) -> ['Flowrate', 'Head']
    [6] = df6(50hz) -> ['Flowrate', 'Head']
    [7] = df7(WellCurve) -> ['Flowrate', 'FBHP']
    [8] = df8(MaxROR) -> ['Flowrate', 'Pressure']
    [9] = df9(MinROR) -> ['Flowrate', 'Pressure']
    [10] = df10(BEP) -> ['Flowrate', 'Pressure']
    """
    #     try:
    sections = {'40Hz', '50Hz', '60Hz', '70Hz', '80Hz', 'WellCurve', 'MaxROR', 'MinROR', 'BEP'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'FunnelCurves')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = cuted_sections[1][1]
    header_3 = cuted_sections[2][1]
    header_4 = cuted_sections[3][1]
    header_5 = cuted_sections[4][1]
    header_6 = cuted_sections[5][1]
    header_7 = cuted_sections[6][1]
    header_8 = cuted_sections[7][1]
    header_9 = cuted_sections[8][1]
    header_10 = cuted_sections[9][1]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = []
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break        
    data_2 = [] # 45hz
    for row in cuted_sections[1][2:]:
        if len(row) > 0 :
            data_2.append(row)
        else:
            break                    
    data_3 = []
    for row in cuted_sections[2][2:]:
        if len(row) > 0 :
            data_3.append(row)
        else:
            break
    data_4 = []
    for row in cuted_sections[3][2:]:
        if len(row) > 0 :
            data_4.append(row)
        else:
            break
    data_5 = []
    for row in cuted_sections[4][2:]:
        if len(row) > 0 :
            data_5.append(row)
        else:
            break
            
    data_6 = []
    for row in cuted_sections[5][2:]:
        if len(row) > 0 :
            data_6.append(row)
        else:
            break
    data_7 = []
    for row in cuted_sections[6][2:]:
        if len(row) > 0 :
            data_7.append(row)
        else:
            break
    data_8 = []
    for row in cuted_sections[7][2:]:
        if len(row) > 0 :
            data_8.append(row)
        else:
            break            
    data_9 = []
    for row in cuted_sections[8][2:]:
        if len(row) > 0 :
            data_9.append(row)
        else:
            break            
    data_10 = []
    for row in cuted_sections[9][2:]:
        if len(row) > 0 :
            data_10.append(row)
        else:
            break            
            
    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1])] for x in data_1]
    data_2 = [[float(x[0]), float(x[1])] for x in data_2]
    data_3 = [[float(x[0]), float(x[1])] for x in data_3]
    data_4 = [[float(x[0]), float(x[1])] for x in data_4]
    data_5 = [[float(x[0]), float(x[1])] for x in data_5] 
    data_6 = [[float(x[0]), float(x[1])] for x in data_6] 
    data_7 = [[float(x[0]), float(x[1])] for x in data_7] 
    data_8 = [[float(x[0]), float(x[1])] for x in data_8] 
    data_9 = [[float(x[0]), float(x[1])] for x in data_9] 
    data_10 = [[float(x[0]), float(x[1])] for x in data_10] 

    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=data_2)
    df3 = pd.DataFrame(columns=header_3, data=data_3)
    df4 = pd.DataFrame(columns=header_4, data=data_4)
    df5 = pd.DataFrame(columns=header_5, data=data_5)
    df6 = pd.DataFrame(columns=header_6, data=data_6)
    df7 = pd.DataFrame(columns=header_7, data=data_7)
    df8 = pd.DataFrame(columns=header_8, data=data_8)
    df9 = pd.DataFrame(columns=header_9, data=data_9)
    df10 = pd.DataFrame(columns=header_10, data=data_10)

    return [doc, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def tornado_curve_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(50Hz) -> ['Flowrate', 'Head']
    [2] = df2(55hz) -> ['Flowrate', 'Head']
    [3] = df3(60hz) -> ['Flowrate', 'Head']
    [4] = df4(62hz) -> ['Flowrate', 'Head']
    [5] = df1(WellCurve) -> ['Flowrate', 'FBHP']
    [6] = df2(MaxROR) -> ['Flowrate', 'Pressure']
    [7] = df3(MinROR) -> ['Flowrate', 'Pressure']
    [8] = df4(BEP) -> ['Flowrate', 'Pressure']
    """
    #     try:
    sections = {'50Hz', '55Hz', '60Hz', '62Hz', 'WellCurve', 'MaxROR', 'MinROR', 'BEP'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'TornadoCurveData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
    header_2 = cuted_sections[1][1]
    header_3 = cuted_sections[2][1]
    header_4 = cuted_sections[3][1]
    header_5 = cuted_sections[4][1]
    header_6 = cuted_sections[5][1]
    header_7 = cuted_sections[6][1]
    header_8 = cuted_sections[7][1]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = []
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break        
    data_2 = [] # 45hz
    for row in cuted_sections[1][2:]:
        if len(row) > 0 :
            data_2.append(row)
        else:
            break                    
    data_3 = []
    for row in cuted_sections[2][2:]:
        if len(row) > 0 :
            data_3.append(row)
        else:
            break
    data_4 = []
    for row in cuted_sections[3][2:]:
        if len(row) > 0 :
            data_4.append(row)
        else:
            break
    data_5 = []
    for row in cuted_sections[4][2:]:
        if len(row) > 0 :
            data_5.append(row)
        else:
            break
            
    data_6 = []
    for row in cuted_sections[5][2:]:
        if len(row) > 0 :
            data_6.append(row)
        else:
            break
    data_7 = []
    for row in cuted_sections[6][2:]:
        if len(row) > 0 :
            data_7.append(row)
        else:
            break
    data_8 = []
    for row in cuted_sections[7][2:]:
        if len(row) > 0 :
            data_8.append(row)
        else:
            break            
      
            
    # Transformando los string a flotante
    data_1 = [[float(x[0]), float(x[1])] for x in data_1]
    data_2 = [[float(x[0]), float(x[1])] for x in data_2]
    data_3 = [[float(x[0]), float(x[1])] for x in data_3]
    data_4 = [[float(x[0]), float(x[1])] for x in data_4]
    data_5 = [[float(x[0]), float(x[1])] for x in data_5] 
    data_6 = [[float(x[0]), float(x[1])] for x in data_6] 
    data_7 = [[float(x[0]), float(x[1])] for x in data_7] 
    data_8 = [[float(x[0]), float(x[1])] for x in data_8] 

    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)
    df2 = pd.DataFrame(columns=header_2, data=data_2)
    df3 = pd.DataFrame(columns=header_3, data=data_3)
    df4 = pd.DataFrame(columns=header_4, data=data_4)
    df5 = pd.DataFrame(columns=header_5, data=data_5)
    df6 = pd.DataFrame(columns=header_6, data=data_6)
    df7 = pd.DataFrame(columns=header_7, data=data_7)
    df8 = pd.DataFrame(columns=header_8, data=data_8)

    return [doc, df1, df2, df3, df4, df5, df6, df7, df8]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def opportunities_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(OpportunitiesContraints) -> ['frequency', 'intersectRate', 'PDP', 'FBHPCalc', 'LimitMotorLoad', 'LimitShaftLoad'
                                            'LimitHousingBurstPressure', 'LimitAllowableFBHP', 'LimitAllowableRate']
    """
    #     try:
    sections = {'OpportunitiesContraints'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'OpportunitiesData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = []
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break       
    # Transformando los string a flotante
    
    if len(data_1[0]) == 8:
        data_1 = [[float(x[0]),
                   float(x[1]),
                   float(x[2]),
                   float(x[3]),
                   float(x[4]),
                   float(x[5]),
                   float(x[6]),
                   float(x[7]),
                   0.0] for x in data_1]
    elif len(data_1) == 9:
        data_1 = [[float(x[0]),
                   float(x[1]),
                   float(x[2]),
                   float(x[3]),
                   float(x[4]),
                   float(x[5]),
                   float(x[6]),
                   float(x[7]),
                   float(x[8])] for x in data_1]   
    else:
        return 'Error en la funcion OpportunitiesData es probable que el numero de columnas difiera de los datos'

    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)

    return [doc, df1]
    #     except:
    #         return 'Error al crear los dataframes, es probable que el patron del archivo sea incorrecto'

def gains_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(GainsData) -> ['Liquid Flowrate Gain', 'Oil Flowrate Gain']
    """
    #     try:
    sections = {'Gains'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'GainsData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = []
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break       
    # Transformando los string a flotante
    
    data_1 = [[float(x[0]), float(x[1]),] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)

    return [doc, df1]
    #     except:    

def predictions_data(data: list) -> list:
    """DOCUMENTATION
    INPUT: data(list) -> Datos de esta seccion en una lista
    OUPUT : [df1](list) -> Lista con los dataframes
    ---"""
    doc = """ESTRUCTURA DEL OUTPUT
    [1] = df1(Predictions) -> ['Predicted Flow rate', 'Fluid above pump', 'Average Tubing Gradient']
    """
    #     try:
    sections = {'Predictions'}

    #  data[1:] porque el primer elemento es el titulo de esta seccion
    cuted_sections = cut_sections(data[1:], sections, 'PredictionsData')
    
    # Filtrando los titulos de la lista
    header_1 = cuted_sections[0][1]
        
    # Filtrando los datos para sus respectivos titulos
    # data[2:] porque apartir de la fila 2 estan los datos
    # los primeros son titulos y columnas
    data_1 = []
    for row in cuted_sections[0][2:]:
        if len(row) > 0 :
            data_1.append(row)
        else:
            break       
    # Transformando los string a flotante
    
    data_1 = [[float(x[0]), float(x[1]), float(x[2]),] for x in data_1]
    
    # Formando los dataframes
    df1 = pd.DataFrame(columns=header_1, data=data_1)

    return [doc, df1]
    #     except:    

def csv_scraper(path: str) -> dict:
    """DOCUMENTATION
    INPUT : document(str) -> Path o ruta del archivo csv a escrapear
    OUTPUT : data(dict) -> Diccionario donde cada llave es una seccion y
    sus valores son listas que contienen dataframes ya estructurados
    """
    #     try:
    headers = {
            'IPRCurveData',
            'ZPlotData',
            'VFDData',
            'BasePumpCurveData',
            'OperatingFrequencyPumpCurveData',
            'DeratedOperatingFrequencyPumpCurveData',
            'OperatingFrequencyInsituPumpCurveData',
            'DeratedOperatingFrequencyInsituPumpCurveData',
            'OperatingPointAnalysisData',
            'FunnelCurves',
            'TornadoCurveData',
            'OpportunitiesData',
            'GainsData',
            'PredictionsData'
    }        

    csv_information = None
    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        csv_information = list(csvreader)
        csvfile.close()

    cuted_sections = cut_sections(csv_information, headers, "PRINCIPAL")   

    data = dict.fromkeys(headers)

    data['IPRCurveData'] = ipr_curve_data(cuted_sections[0])
    data['ZPlotData'] = z_plot_data(cuted_sections[1])
    data['VFDData'] = vfd_data(cuted_sections[2])
    data['BasePumpCurveData'] = base_pump_curve_data(cuted_sections[3])
    data['OperatingFrequencyPumpCurveData'] = operating_freq_pump_curve_data(cuted_sections[4])
    data['DeratedOperatingFrequencyPumpCurveData'] = derated_operating_freq_pump_curve_data(cuted_sections[5])
    data['OperatingFrequencyInsituPumpCurveData'] = operating_freq_insitu_pump_curve_data(cuted_sections[6])
    data['DeratedOperatingFrequencyInsituPumpCurveData'] = derated_operating_freq_insitu_pump_curve_data(cuted_sections[7])
    data['OperatingPointAnalysisData'] = operating_point_analysis_data(cuted_sections[8])
    data['FunnelCurves'] = funnel_curves(cuted_sections[9])
    data['TornadoCurveData'] = tornado_curve_data(cuted_sections[10])
    data['OpportunitiesData'] = opportunities_data(cuted_sections[11])
    data['GainsData'] = gains_data(cuted_sections[12])
    data['PredictionsData'] = predictions_data(cuted_sections[13])
    return data
    #     except:
    #         print('Es probable que la ruta del documento sea invalida')
