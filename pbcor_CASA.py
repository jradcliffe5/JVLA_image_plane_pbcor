from recipes import makepb
import sys, os

try:
	msfile = str(sys.argv[sys.argv.index('pbcor_CASA.py')+1])
	imagetemplate = str(sys.argv[sys.argv.index('pbcor_CASA.py')+2])
except IndexError:
	print('Usage casa -c pbcor_CASA.py <msfile> <image>')

print '\npbcor_CASA generating images for your VLA needs and wants, huzzah\n'
if imagetemplate[-1] == '/':
	imagetemplate = imagetemplate[:-1]

if imagetemplate[-4:]== 'fits' or imagetemplate[-4:]=='FITS':
	print 'FITS file detected - converting to ms\n'
	importfits(fitsimage=imagetemplate, imagename=imagetemplate[:-4]+'image')
	imagetemplate = imagetemplate[:-4]+'image'

	print 'Using makepb recipe to generate pb\n'
	makepb.makePB(vis=msfile,field='0',imtemplate=imagetemplate,outimage=msfile[:-2]+'pb',pblimit=0.1)

	print 'Primary beam correcting image, new pbcor image = %s\n' % imagetemplate[:-6]+'_pbcor.image'
	impbcor(imagename=imagetemplate, pbimage=msfile[:-2]+'pb', outfile=imagetemplate[:-6]+'_pbcor.image')

	print 'Exporting to pb and pbcor image to fits\n'
	exportfits(imagename=imagetemplate[:-6]+'_pbcor.image', fitsimage=imagetemplate[:-6]+'_pbcor.fits')
	exportfits(imagename=msfile[:-2]+'pb', fitsimage=msfile[:-2]+'pb.fits')
else:
	print 'No fits file detected, assuming image name is CASA image... sorry\n'
	makepb.makePB(vis=msfile,field='0',imtemplate=imagetemplate,outimage=msfile[:-2]+'pb',pblimit=0.1)

	print 'Primary beam correcting image, new pbcor image = %s\n' % imagetemplate+'.pbcor'
	impbcor(imagename=imagetemplate, pbimage=msfile[:-2]+'pb', outfile=imagetemplate+'_pbcor')
	print 'Exporting to pb and pbcor image to fits\n'
	exportfits(imagename=imagetemplate+'.pbcor', fitsimage=imagetemplate+'.pbcor.fits')
	exportfits(imagename=msfile[:-2]+'pb', fitsimage=msfile[:-2]+'pb.fits')
