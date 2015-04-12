#include "Geometry/HcalTowerAlgo/interface/HcalParametersFromDD.h"
#include "CondFormats/GeometryObjects/interface/PHcalParameters.h"
#include "DetectorDescription/Core/interface/DDCompactView.h"
#include "DetectorDescription/Core/interface/DDVectorGetter.h"
#include "DetectorDescription/Base/interface/DDutils.h"

bool
HcalParametersFromDD::build( const DDCompactView* cvp,
			     PHcalParameters& php)
{
  php.phioff = DDVectorGetter::get( "phioff" );
  php.etaTable = DDVectorGetter::get( "etaTable" );
  php.rTable = DDVectorGetter::get( "rTable" );
  php.phibin = DDVectorGetter::get( "phibin" );
  php.phitable = DDVectorGetter::get( "phitable" );  
  php.etaRange = DDVectorGetter::get( "etaRange" );
  php.gparHF = DDVectorGetter::get( "gparHF" );
  php.noff = dbl_to_int( DDVectorGetter::get( "noff" ));
  php.Layer0Wt = DDVectorGetter::get( "Layer0Wt" );  
  php.HBGains = DDVectorGetter::get( "HBGains" );
  php.HEGains = DDVectorGetter::get( "HEGains" );
  php.HFGains = DDVectorGetter::get( "HFGains" );
  php.etaMin = dbl_to_int( DDVectorGetter::get( "etaMin" ));
  php.etaMax = dbl_to_int( DDVectorGetter::get( "etaMax" ));
  php.HBShift = dbl_to_int( DDVectorGetter::get( "HBShift" ));
  php.HEShift = dbl_to_int( DDVectorGetter::get( "HEShift" ));
  php.HFShift = dbl_to_int( DDVectorGetter::get( "HFShift" ));

  php.etagroup = dbl_to_int( DDVectorGetter::get( "etagroup" ));
  php.phigroup = dbl_to_int( DDVectorGetter::get( "phigroup" ));
			      
  PHcalParameters::LayerItem layerGroupEta;
  for( unsigned int i = 0; i < 27; ++i )
  {
    std::stringstream sstm;
    sstm << "layerGroupEta" << i;
    std::string tempName = sstm.str();

    if( DDVectorGetter::check( tempName ))
    {
      PHcalParameters::LayerItem layerGroupEta;
      layerGroupEta.layer = i;
      layerGroupEta.layerGroup = dbl_to_int( DDVectorGetter::get( tempName ));
      php.layerGroupEta.push_back( layerGroupEta );
    }
  }

  int topologyMode = 0;
  php.topologyMode = topologyMode;

  return true;
}