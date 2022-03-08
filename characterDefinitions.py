#--Can add new definitions here to apply this code to other problems or datasets.--
import numpy as np

def getHandwritingCharacterDefinitions():
    """
    Returns a dictionary with entries that define the names of each character, its length, and where the pen tip begins.
    
    Returns:
        charDef (dict)
    """
        
    charDef = {}
    
    #Define the list of all 31 characters and their names.
    charDef['charList'] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'greaterThan','comma','apostrophe','tilde','questionMark']
    charDef['charListAbbr'] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                '>',',',"'",'~','?']

 #   charDef['charLen'] = np.array([157,205,115,196,139,178,229,151, 85,145,151, 82,232,133,136,232,205,121,169,184,121,145,232,136, 88,75, 55, 58, 28,91,256]).astype(np.int32)
    #Define the length of each character (in # of 10 ms bins) to use for each template.
    #These were hand-defined based on visual inspection of the reconstructed pen trajectories.
 #   charDef['charLen'] = np.array([157,181,89,203,144,173,212,160,90,171,182,76,251,145,125,203,197,118,143,158,136,124,207,124,177,158,157,41,29,91,150]).astype(np.int32)
 #   charDef['charLen']=np.array([105, 121, 59, 135, 96, 115, 142, 107, 60, 114, 122, 51, 168, 97, 83, 135, 132, 79, 95, 106, 91, 83, 138, 83, 118, 106, 105, 28, 20, 61, 100])
    

  #  charDef['charLen']=np.array([-5, -46, -103, -18, -84,   -34, -15, -70, -108, -90, -64,    -98, 2,  -75,  -80, -65, -45,  -85,  -50, -82,  -68, -84, -48,  11, 53, 10,    -150,  -150,  -150,  -150, -125]) # Interp by 3 (Adjusted)
  #  charDef['charLen']=charDef['charLen']+175
    
 #   charDef['charLen']=np.array([-34, -51, -131, -39, -102,   -115, 10, -75, -137, -90, -64,    -116, 2,  -89,  -112, -42, -45,  -119,  -88, -98,  -108, -70, -55,  11, -105, 10,    -166,  -166,  -177,  -166, -135]) # Interp by 3 (Adjusted)
 #   charDef['charLen']=charDef['charLen']+214
    
 #   charDef['charLen']=np.array([-31, -51, -131, -39, -112,   -73, 10, -98, -141, -90, -64,    -120, 2,  -99,  -119, -48, 10,  -119,  -102, -94,  -82, -70, -88,  -40, -90, -40,    -166,  -166,  -177,  -166, -135]) # Interp by 3 (Adjusted)
  #  charDef['charLen']=charDef['charLen']+249
    
    charDef['charLen']=np.array([-31, -99, -136, -44, -109,   -73, -106, -105, -163, -90, -115,    -161, -27,  -111,  -122, -68, -35,  -138,  -130, -105,  -82, -70, -107,  -40, -122, -40,    -166,  -166,  -177,  -166, -135]) # Interp by 3 (Adjusted)
    charDef['charLen']=charDef['charLen']+250

    
    #For each character, this defines the starting location of the pen tip (0 = bottom of the line, 1 = top)
    charDef['penStart'] = [0.25, 1, 0.5, 0.5, 0.25, 1.0, 0.25, 1.0, 0.5, 0.5, 1, 1, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 1, 
           0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 1, 0.5, 1]
    
    #dictionary to convert string representation to character index
    charDef['strToCharIdx'] = {}
    for x in range(len(charDef['charListAbbr'])):
        charDef['strToCharIdx'][charDef['charListAbbr'][x]] = x
        
    #ordering of characters that kaldi (i.e., the language model) expects
    charDef['kaldiOrder'] = ['<ctc>','>',"'",',','.','?','a','b','c','d','e','f','g','h','i','j',
                             'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    #re-indexing to match kaldi order (e.g., outputs[:,:,charDef['idxToKaldi']] places the output in kald-order)
    charDef['idxToKaldi'] = np.array([31,26,28,27,29,30,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                     21,22,23,24,25]).astype(np.int32)
    
    return charDef