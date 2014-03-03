import FWCore.ParameterSet.Config as cms

from SimGeneral.MixingModule.ecalTimeDigitizer_cfi import *

def cust_ecalTime(process):
    # Store layer in 1 cm for ECAL and 1ps timeSlices
    if hasattr(process,'g4SimHits'):
        print "___ EcalSD configured for 1ps time resolution and 1cm layers ___"
        process.g4SimHits.ECalSD.StoreLayerTimeSim  = cms.untracked.bool(True)
        process.g4SimHits.ECalSD.TimeSliceUnit  = cms.double(0.001)

    # Switch on the ecalTime digitization
    if hasattr(process,'mix'):
        if ( hasattr( getattr( getattr( process, 'mix'), 'digitizers' ), 'ecal' ) ):
            print "___ Adding ecalDetailedTime digitizer ___"
            process.mix.digitizers.ecalTime=cms.PSet(
                ecalTimeDigitizer
                )

    if hasattr(process,'reconstruction_step'):
        print "___ Adding ecalDetailedTimeRecHit associator ___"
        process.load("RecoLocalCalo.EcalRecProducers.ecalDetailedTimeRecHit_cfi")
        process.reconstruction_step+=process.ecalDetailedTimeRecHit
        
#        process.ecalRecHitSequence += 

    # Special PU files (temporary)
    if hasattr ( process, 'mix' ):
        if ( hasattr( getattr( process, 'mix'), 'input' ) ):
            print "___ Adding MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE PU files ___"
            process.mix.input.fileNames = cms.untracked.vstring( [
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_9_1_Vay.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_99_1_r02.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_98_1_t0g.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_97_1_DMK.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_96_1_bhG.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_95_1_sAa.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_94_1_xGH.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_93_1_aHB.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_92_1_9Ek.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_91_1_Uwc.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_90_1_BUx.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_8_1_dQv.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_89_1_YJO.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_88_1_Uai.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_87_1_HTD.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_86_1_B1S.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_85_1_FqG.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_84_1_MYt.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_83_1_qTB.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_82_1_nCW.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_81_1_Hek.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_80_1_Vz0.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_7_1_VxT.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_79_1_XGY.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_78_1_v2n.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_77_1_rcu.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_76_1_6uu.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_75_1_lAy.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_74_1_zUb.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_73_1_xQr.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_72_1_MHn.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_71_1_qjz.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_70_1_PCv.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_6_1_Jnv.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_69_1_f2d.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_67_1_3Kn.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_66_1_99A.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_65_1_HaB.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_64_1_5jn.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_63_1_eCo.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_62_1_YIY.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_61_1_7qu.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_60_1_TNh.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_5_1_P9I.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_59_1_Qkr.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_58_1_vKw.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_57_1_hSj.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_56_1_LQ1.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_55_1_k5F.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_54_1_srz.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_53_1_mPn.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_52_1_zL9.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_51_1_qHI.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_50_1_Syg.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_4_1_JV4.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_49_1_EBK.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_48_1_GSb.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_47_1_XPc.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_46_1_XbZ.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_45_1_8vZ.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_44_1_pC0.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_43_1_Vf7.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_42_1_m57.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_41_1_OWS.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_40_1_qJD.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_3_1_qjS.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_39_1_nGL.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_38_1_H18.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_37_1_9FT.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_36_1_2RW.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_35_1_Xx1.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_34_1_L0b.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_33_1_Dne.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_32_1_PDr.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_31_1_ddL.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_30_1_fiF.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_2_1_qhg.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_29_1_GY2.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_28_1_kmC.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_27_1_uMu.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_26_1_gNZ.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_25_1_89M.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_24_1_SPH.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_23_1_VYl.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_22_1_VDT.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_21_1_quB.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_20_1_O64.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_1_1_BT4.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_19_1_iQR.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_18_1_yge.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_17_1_Y2J.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_16_1_dMT.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_15_1_9KG.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_14_1_z38.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_12_1_94t.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_11_1_zcJ.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_10_1_Grd.root",
                "/store/caf/user/meridian/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/MinBias_TuneZ2star_14TeV_pythia6_620SLHC4_UPG2017ECALFINE_b/ccc0d0fec5febc34ed7e51dc9420a40b/MinBias_TuneZ2star_14TeV_pythia6_GEN_SIM_100_1_lfB.root"
                ] )
            print "___ Loaded "+str(len(process.mix.input.fileNames))+" files  ___"
#    for file in process.mix.input.fileNames:
#        print file

    return(process)




    
