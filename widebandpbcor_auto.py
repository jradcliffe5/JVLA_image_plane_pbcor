import numpy as np
import os
#### Inputs ####
msfile = 'JVLA1_small_data.ms'
#imagename = 'HDFC0015'

for file in os.listdir('./'):
    if file.endswith('.image.tt0'):
        imagename = file.split('.image.tt0')[0]
        os.system('rm -r %s.pbcor*' % imagename)
        print imagename
        tb.open(msfile+'/SPECTRAL_WINDOW')
        x = tb.getcol('NUM_CHAN')
        tb.close()
        nospw = len(x)
        spwlist = np.linspace(0,nospw-1,nospw).astype(int)
        chanlist = (np.ones(nospw)*int(x[0]/2.)).astype(int)
        weightlist = np.ones(nospw)

        widebandpbcor(vis=msfile,imagename=imagename,nterms=2,threshold="",action="pbcor",reffreq="",pbmin=0.2,field="",spwlist=spwlist,chanlist=chanlist,weightlist=weightlist)
