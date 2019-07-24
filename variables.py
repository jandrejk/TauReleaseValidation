vardict = {

    #============================================================================================================================
    #   discrimination of tau leptons against muons (see https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV#Muon_Rejection)
    #============================================================================================================================
    'againstMuonLoose3': {'var': 'tau_againstMuonLoose3 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstMuonLoose3'},
    'againstMuonTight3': {'var': 'tau_againstMuonTight3 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstMuonTight3'},

    #============================================================================================================================
    #   discrimination of tau leptons against electrons (see https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV#Electron_Rejection)
    #============================================================================================================================
    'againstElectronVLooseMVA6': {'var': 'tau_againstElectronVLooseMVA6 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstElectronVLooseMVA6'},
    'againstElectronLooseMVA6': {'var': 'tau_againstElectronLooseMVA6 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstElectronLooseMVA6'},
    'againstElectronMediumMVA6': {'var': 'tau_againstElectronMediumMVA6 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstElectronMediumMVA6'},
    'againstElectronTightMVA6': {'var': 'tau_againstElectronVLooseMVA6 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstElectronTightMVA6'},
    'againstElectronVThightMVA6': {'var': 'tau_againstElectronLooseMVA6 > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'againstElectronVTightMVA6'},

    






    'oldDecayModeFinding': {'var': 'tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'oldDecayModeFinding'},
    'newDecayModeFinding': {'var': 'tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'newDecayModeFinding'},
    #'oldDecayModeFindingModified':{'var':'tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'oldDecayModeFinding w/ 3p+#pi^{0}'},
    'oldDecayModeFindingModified': {'var': '(tau_decayModeFinding > 0.5 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'oldDecayModeFinding w/ 3p+#pi^{0}'},

    # oldDM
    #'byLoosePileupWeightedIsolation3Hits':{'var':'tau_byLoosePileupWeightedIsolation3Hits > 0.5 && tau_decayModeFinding > 0.5', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'byLoosePileupWeightedIsolation3Hits'},
    #'byMediumPileupWeightedIsolation3Hits':{'var':'tau_byMediumPileupWeightedIsolation3Hits > 0.5 && tau_decayModeFinding > 0.5', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'byMediumPileupWeightedIsolation3Hits'},
    #'byTightPileupWeightedIsolation3Hits':{'var':'tau_byTightPileupWeightedIsolation3Hits > 0.5 && tau_decayModeFinding > 0.5', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'byTightPileupWeightedIsolation3Hits'},

    'byLooseCombinedIsolationDeltaBetaCorr3Hits': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation': {'var': 'tau_chargedIsoPtSum < 2.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation': {'var': 'tau_chargedIsoPtSum < 1.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation': {'var': 'tau_chargedIsoPtSum < 0.8 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr': {'var': 'tau_neutralIsoPtSum < 6 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr': {'var': 'tau_neutralIsoPtSum < 5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr': {'var': 'tau_neutralIsoPtSum < 4 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},

    #'byLooseIsolationMVA3oldDMwLT':{'var':'tau_byLooseIsolationMVA3oldDMwLT > 0.5 && tau_decayModeFinding > 0.5', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'byLooseIsolationMVA3oldDMwLT'},
    #'byMediumIsolationMVA3oldDMwLT':{'var':'tau_byMediumIsolationMVA3oldDMwLT > 0.5 && tau_decayModeFinding > 0.5', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'byMediumIsolationMVA3oldDMwLT'},
    #'byTightIsolationMVA3oldDMwLT':{'var':'tau_byTightIsolationMVA3oldDMwLT > 0.5 && tau_decayModeFinding > 0.5', 'nbin':2, 'min':-0.5, 'max':1.5, 'title':'byTightIsolationMVA3oldDMwLT'},

    # this still exists 
    'byLooseIsolationMVArun2v1DBoldDMwLT':  {'var': 'tau_byLooseIsolationMVArun2v1DBoldDMwLT  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1DBoldDMwLT'},
    'byMediumIsolationMVArun2v1DBoldDMwLT': {'var': 'tau_byMediumIsolationMVArun2v1DBoldDMwLT > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1DBoldDMwLT'},
    'byTightIsolationMVArun2v1DBoldDMwLT':  {'var': 'tau_byTightIsolationMVArun2v1DBoldDMwLT  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1DBoldDMwLT'},
    # still exists
    'byLooseIsolationMVArun2v1PWoldDMwLT':  {'var': 'tau_byLooseIsolationMVArun2v1PWoldDMwLT  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1PWoldDMwLT'},
    'byMediumIsolationMVArun2v1PWoldDMwLT': {'var': 'tau_byMediumIsolationMVArun2v1PWoldDMwLT > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1PWoldDMwLT'},
    'byTightIsolationMVArun2v1PWoldDMwLT':  {'var': 'tau_byTightIsolationMVArun2v1PWoldDMwLT  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1PWoldDMwLT'},
    
    # # 2017v1
    # 'byLooseIsolationMVArun2017v1DBoldDMwLT2017':  {'var': 'tau_byLooseIsolationMVArun2017v1DBoldDMwLT2017  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2017v1DBoldDMwLT2017'},
    # 'byMediumIsolationMVArun2017v1DBoldDMwLT2017': {'var': 'tau_byMediumIsolationMVArun2017v1DBoldDMwLT2017 > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2017v1DBoldDMwLT2017'},
    # 'byTightIsolationMVArun2017v1DBoldDMwLT2017':  { 'var': 'tau_byTightIsolationMVArun2017v1DBoldDMwLT2017  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2017v1DBoldDMwLT2017'},
    # # 2017v2
    # 'byLooseIsolationMVArun2017v2DBoldDMwLT2017':  { 'var': 'tau_byLooseIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2017v2DBoldDMwLT2017'},
    # 'byMediumIsolationMVArun2017v2DBoldDMwLT2017': {'var': 'tau_byMediumIsolationMVArun2017v2DBoldDMwLT2017 > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2017v2DBoldDMwLT2017'},
    # 'byTightIsolationMVArun2017v2DBoldDMwLT2017':  { 'var': 'tau_byTightIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2017v2DBoldDMwLT2017'},
    # # 2016v1
    # "byLooseIsolationMVArun2v1DBoldDMwLT2016":  { 'var': 'tau_byLooseIsolationMVArun2v1DBoldDMwLT2016  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1DBoldDMwLT2016'},
    # 'byMediumIsolationMVArun2v1DBoldDMwLT2016': {'var': 'tau_byMediumIsolationMVArun2v1DBoldDMwLT2016 > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1DBoldDMwLT2016'},
    # 'byTightIsolationMVArun2v1DBoldDMwLT2016':  { 'var': 'tau_byTightIsolationMVArun2v1DBoldDMwLT2016  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1DBoldDMwLT2016'},
    # # 2017v2 dR=0.3
    # "byLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017": {'var': 'tau_byLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017'},
    # 'byMediumIsolationMVArun2017v2DBoldDMdR0p3wLT2017': {'var': 'tau_byMediumIsolationMVArun2017v2DBoldDMdR0p3wLT2017 > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2017v2DBoldDMdR0p3wLT2017'},
    # 'byTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017':  {'var': 'tau_byTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017  > 0.5 && tau_decayModeFinding > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2017v2DBoldDMdR0p3wLT2017'},

    # newDM
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_newDM': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_newDM': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_newDM': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_newDM': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_newDM': {'var': 'tau_chargedIsoPtSum < 2.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_newDM': {'var': 'tau_chargedIsoPtSum < 1.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_newDM': {'var': 'tau_chargedIsoPtSum < 0.8 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_newDM': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_newDM': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_newDM': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_newDM': {'var': 'tau_neutralIsoPtSum < 6 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_newDM': {'var': 'tau_neutralIsoPtSum < 5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_newDM': {'var': 'tau_neutralIsoPtSum < 4 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},
    # 2016 new
    # "byLooseIsolationMVArun2v1DBnewDMwLT2016": {'var': 'tau_byLooseIsolationMVArun2v1DBnewDMwLT2016  > 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1DBnewDMwLT2016'},
    # 'byMediumIsolationMVArun2v1DBnewDMwLT2016': {'var': 'tau_byMediumIsolationMVArun2v1DBnewDMwLT2016 > 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1DBnewDMwLT2016'},
    # 'byTightIsolationMVArun2v1DBnewDMwLT2016':  {'var': 'tau_byTightIsolationMVArun2v1DBnewDMwLT2016  > 0.5 && tau_decayModeFindingNewDMs > 0.5', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1DBnewDMwLT2016'},

    # modOldDM
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_modOldDM': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_modOldDM': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_modOldDM': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_modOldDM': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_modOldDM': {'var': 'tau_chargedIsoPtSum < 2.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_modOldDM': {'var': 'tau_chargedIsoPtSum < 1.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_modOldDM': {'var': 'tau_chargedIsoPtSum < 0.8 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_modOldDM': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_modOldDM': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_modOldDM': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_modOldDM': {'var': 'tau_neutralIsoPtSum < 6 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_modOldDM': {'var': 'tau_neutralIsoPtSum < 5 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_modOldDM': {'var': 'tau_neutralIsoPtSum < 4 && tau_decayModeFindingNewDMs > 0.5 && tau_dm != 5 && tau_dm != 6', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},


    # 1prong
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_1p': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_1p': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_1p': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_1p': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_1p': {'var': 'tau_chargedIsoPtSum < 2.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_1p': {'var': 'tau_chargedIsoPtSum < 1.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_1p': {'var': 'tau_chargedIsoPtSum < 0.8 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_1p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_1p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_1p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_1p': {'var': 'tau_neutralIsoPtSum < 6 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_1p': {'var': 'tau_neutralIsoPtSum < 5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_1p': {'var': 'tau_neutralIsoPtSum < 4 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},

    'byLooseIsolationMVArun2v1DBoldDMwLT_1p':  {'var': 'tau_byLooseIsolationMVArun2v1DBoldDMwLT  > 0.5  && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1DBoldDMwLT_1p'},
    'byMediumIsolationMVArun2v1DBoldDMwLT_1p': {'var': 'tau_byMediumIsolationMVArun2v1DBoldDMwLT > 0.5  && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1DBoldDMwLT_1p'},
    'byTightIsolationMVArun2v1DBoldDMwLT_1p':  {'var': 'tau_byTightIsolationMVArun2v1DBoldDMwLT  > 0.5  && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1DBoldDMwLT_1p'},
    
    # 'byLooseIsolationMVArun2017v2DBoldDMwLT2017_1p':  {'var': 'tau_byLooseIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2017v2DBoldDMwLT2017_1p'},
    # 'byMediumIsolationMVArun2017v2DBoldDMwLT2017_1p': {'var': 'tau_byMediumIsolationMVArun2017v2DBoldDMwLT2017 > 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2017v2DBoldDMwLT2017_1p'},
    # 'byTightIsolationMVArun2017v2DBoldDMwLT2017_1p':  {'var': 'tau_byTightIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && tau_dm == 0', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2017v2DBoldDMwLT2017_1p'},

    # 1prong+pi0's
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_1ppi0': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_1ppi0': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_1ppi0': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_1ppi0': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_1ppi0': {'var': 'tau_chargedIsoPtSum < 2.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_1ppi0': {'var': 'tau_chargedIsoPtSum < 1.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_1ppi0': {'var': 'tau_chargedIsoPtSum < 0.8 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_1ppi0': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_1ppi0': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_1ppi0': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_1ppi0': {'var': 'tau_neutralIsoPtSum < 6 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_1ppi0': {'var': 'tau_neutralIsoPtSum < 5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_1ppi0': {'var': 'tau_neutralIsoPtSum < 4 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},

    'byLooseIsolationMVArun2v1DBoldDMwLT_1ppi0':  {'var': 'tau_byLooseIsolationMVArun2v1DBoldDMwLT  > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1DBoldDMwLT_1ppi0'},
    'byMediumIsolationMVArun2v1DBoldDMwLT_1ppi0': {'var': 'tau_byMediumIsolationMVArun2v1DBoldDMwLT > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1DBoldDMwLT_1ppi0'},
    'byTightIsolationMVArun2v1DBoldDMwLT_1ppi0':  {'var': 'tau_byTightIsolationMVArun2v1DBoldDMwLT  > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1DBoldDMwLT_1ppi0'},
    
    # 'byLooseIsolationMVArun2017v2DBoldDMwLT2017_1ppi0':  {'var': 'tau_byLooseIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2017v2DBoldDMwLT2017_1ppi0'},
    # 'byMediumIsolationMVArun2017v2DBoldDMwLT2017_1ppi0': {'var': 'tau_byMediumIsolationMVArun2017v2DBoldDMwLT2017 > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2017v2DBoldDMwLT2017_1ppi0'},
    # 'byTightIsolationMVArun2017v2DBoldDMwLT2017_1ppi0':  {'var': 'tau_byTightIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2017v2DBoldDMwLT2017_1ppi0'},

    # 2prongs
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_2p': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_2p': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_2p': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_2p': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_2p': {'var': 'tau_chargedIsoPtSum < 2.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_2p': {'var': 'tau_chargedIsoPtSum < 1.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_2p': {'var': 'tau_chargedIsoPtSum < 0.8 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_2p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_2p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_2p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_2p': {'var': 'tau_neutralIsoPtSum < 6 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_2p': {'var': 'tau_neutralIsoPtSum < 5 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_2p': {'var': 'tau_neutralIsoPtSum < 4 && (tau_dm == 5 || tau_dm==6)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},

    # 3prongs
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_3p': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_3p': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_3p': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_3p': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_3p': {'var': 'tau_chargedIsoPtSum < 2.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_3p': {'var': 'tau_chargedIsoPtSum < 1.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_3p': {'var': 'tau_chargedIsoPtSum < 0.8 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_3p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_3p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_3p': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_3p': {'var': 'tau_neutralIsoPtSum < 6 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_3p': {'var': 'tau_neutralIsoPtSum < 5 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_3p': {'var': 'tau_neutralIsoPtSum < 4 && (tau_dm == 10 || tau_dm == 11)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},

    # 3prongs classic
    'byLooseCombinedIsolationDeltaBetaCorr3Hits_3pold': {'var': 'tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseCombinedIsolationDeltaBetaCorr3Hits'},
    'byMediumCombinedIsolationDeltaBetaCorr3Hits_3pold': {'var': 'tau_byMediumCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumCombinedIsolationDeltaBetaCorr3Hits'},
    'byTightCombinedIsolationDeltaBetaCorr3Hits_3pold': {'var': 'tau_byTightCombinedIsolationDeltaBetaCorr3Hits > 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightCombinedIsolationDeltaBetaCorr3Hits'},

    'byPtOutOfCone_3pold': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt < 0.1 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'out-of-cone-Pt/Pt < 0.1'},
    'byLooseChargedIsolation_3pold': {'var': 'tau_chargedIsoPtSum < 2.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 2.5 GeV'},
    'byMediumChargedIsolation_3pold': {'var': 'tau_chargedIsoPtSum < 1.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 1.5 GeV'},
    'byTightChargedIsolation_3pold': {'var': 'tau_chargedIsoPtSum < 0.8 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'charged iso < 0.8 GeV'},
    'byLooseNeutralIsolation_3pold': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1.5 GeV'},
    'byMediumNeutralIsolation_3pold': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 1.0 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 1 GeV'},
    'byTightNeutralIsolation_3pold': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum) < 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': '(neutral-iso - 0.2*PU-Pt-Sum) < 0.5 GeV'},
    'byLooseNeutralIsolationUnCorr_3pold': {'var': 'tau_neutralIsoPtSum < 6 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 6 GeV'},
    'byMediumNeutralIsolationUnCorr_3pold': {'var': 'tau_neutralIsoPtSum < 5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 5 GeV'},
    'byTightNeutralIsolationUnCorr_3pold': {'var': 'tau_neutralIsoPtSum < 4 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'neutral-iso < 4 GeV'},

    'byLooseIsolationMVArun2v1DBoldDMwLT_3pold':  {'var': 'tau_byLooseIsolationMVArun2v1DBoldDMwLT  > 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2v1DBoldDMwLT_3pold'},
    'byMediumIsolationMVArun2v1DBoldDMwLT_3pold': {'var': 'tau_byMediumIsolationMVArun2v1DBoldDMwLT > 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2v1DBoldDMwLT_3pold'},
    'byTightIsolationMVArun2v1DBoldDMwLT_3pold':  {'var': 'tau_byTightIsolationMVArun2v1DBoldDMwLT  > 0.5 && tau_dm == 10', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2v1DBoldDMwLT_3pold'},
    
    # does not exist anymore
    # 'byLooseIsolationMVArun2017v2DBoldDMwLT2017_3pold':  {'var': 'tau_byLooseIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byLooseIsolationMVArun2017v2DBoldDMwLT2017_3pold'},
    # 'byMediumIsolationMVArun2017v2DBoldDMwLT2017_3pold': {'var': 'tau_byMediumIsolationMVArun2017v2DBoldDMwLT2017 > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byMediumIsolationMVArun2017v2DBoldDMwLT2017_3pold'},
    # 'byTightIsolationMVArun2017v2DBoldDMwLT2017_3pold':  {'var': 'tau_byTightIsolationMVArun2017v2DBoldDMwLT2017  > 0.5 && (tau_dm == 1 || tau_dm == 2)', 'nbin': 2, 'min': -0.5, 'max': 1.5, 'title': 'byTightIsolationMVArun2017v2DBoldDMwLT2017_3pold'},
}

hvardict = {
    'charged_isoPt': {'var': 'tau_chargedIsoPtSum', 'nbin': 20, 'min': 0., 'max': 10, 'title': 'charged iso [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'charged_isoPtNoPV': {'var': 'tau_iso_nopv', 'nbin': 20, 'min': 0., 'max': 10, 'title': 'charged iso (noPV) [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'charged_isoPt02':{'var':'tau_iso_dz02', 'nbin':20, 'min':0., 'max':10, 'title':'charged iso (|dz|<0.2cm) [GeV]', 'sel':'tau_genpt>0&&tau_pt>0'},
    'charged_isoPtNoPV_frac': {'var': 'tau_iso_nopv/(tau_iso_dz02+0.005)', 'nbin': 20, 'min': 0., 'max': 1, 'title': 'charged iso npPV fraction', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'charged_isoPtPV': {'var': 'tau_iso_pv', 'nbin': 20, 'min': 0., 'max': 10, 'title': 'charged iso (PV) [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'charged_isoPt_diff': {'var': '2.*(tau_chargedIsoPtSum-tau_iso_dz02)/(tau_chargedIsoPtSum+tau_iso_dz02)', 'nbin': 40, 'min': -2., 'max': 2, 'title': '2*(charged iso-iso02)/(charged iso+iso02)', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_chargedIsoPtSum+tau_iso_dz02>0'},
    
    'nPU': {'var': 'tau_nPU', 'nbin': 100, 'min': 0., 'max': 100, 'title': 'no. of pileup', 'sel': '1'},
    'nVertex': {'var': 'tau_vertex', 'nbin': 100, 'min': 0., 'max': 100, 'title': 'no. of vertices', 'sel': '1'},

    'neutral_isoPt': {'var': 'tau_neutralIsoPtSum', 'nbin': 20, 'min': 0., 'max': 10, 'title': 'neutral iso [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'neutral_isoPt_corr': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum)', 'nbin': 20, 'min': 0, 'max': 10, 'title': 'neutral-iso - 0.2*PU-Pt-Sum [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'neutral_isoPt_corr2': {'var': 'max(0,tau_neutralIsoPtSum-0.2*tau_puCorrPtSum)', 'nbin': 20, 'min': 0, 'max': 10, 'title': 'out-of-cone-Pt/Pt < 0.1; neutral-iso - 0.2*PU-Pt-Sum [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_photonPtSumOutsideSignalCone/tau_pt<0.1'},
    'neutral_isoPt_diff': {'var': '2.*(tau_neutralIsoPtSum-tau_iso_neu)/(tau_neutralIsoPtSum+tau_iso_neu)', 'nbin': 40, 'min': -2., 'max': 2, 'title': '2*(neutral iso AOD-MiniAOD)/(neutral iso AOD+MiniAOD)', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_neutralIsoPtSum+tau_iso_neu>0'},
    
    'outOfConePt_over_pt': {'var': 'tau_photonPtSumOutsideSignalCone/tau_pt', 'nbin': 25, 'min': 0., 'max': 0.25, 'title': 'out-of-cone-Pt/Pt', 'sel': 'tau_genpt>0&&tau_pt>0'},
    
    'pu_isoPt': {'var': 'tau_puCorrPtSum', 'nbin': 50, 'min': 0., 'max': 100, 'title': 'PU charged PtSum [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},
    
    'tau_CombIsoRaw': {'var': 'tau_byCombinedIsolationDeltaBetaCorrRaw3Hits', 'nbin': 20, 'min': 0., 'max': 10, 'title': 'combined iso (oldDMs) (GeV)', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_decayModeFinding > 0.5'},
    
    'tau_MVA':     {    'var': 'tau_byIsolationMVArun2v1DBoldDMwLTraw', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    'tau_MVAIsoRaw':   {'var': 'tau_byIsolationMVArun2v1DBoldDMwLTraw', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    'tau_MVAIsoRawPW': {'var': 'tau_byIsolationMVArun2v1PWoldDMwLTraw', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    'tau_MVAIsoRawdR03': {'var': 'tau_byIsolationMVArun2v1DBdR03oldDMwLTraw', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    
    'tau_dm': {'var': 'tau_dm', 'nbin': 12, 'min': 0., 'max': 12, 'title': 'decay Mode', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'tau_dm_chiso': {'var': 'tau_dm', 'nbin': 12, 'min': 0., 'max': 12, 'title': 'decay Mode', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_chargedIsoPtSum < 2.5'},
    'tau_dm_combiso': {'var': 'tau_dm', 'nbin': 12, 'min': 0., 'max': 12, 'title': 'decay Mode', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_byLooseCombinedIsolationDeltaBetaCorr3Hits > 0.5'},
    
    'tau_dxy': {'var': 'tau_dxy', 'nbin': 50, 'min': 0., 'max': 0.1, 'title': 'tau_dxy', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'tau_dxy_err': {'var': 'tau_dxy_err', 'nbin': 40, 'min': 0., 'max': 0.02, 'title': 'tau_dxy_err', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'tau_dxy_sig': {'var': 'tau_dxy_sig', 'nbin': 25, 'min': 0., 'max': 5, 'title': 'tau_dxy_sig', 'sel': 'tau_genpt>0&&tau_pt>0'},
    
    'tau_eta': {'var': 'tau_eta', 'nbin': 12, 'min': -2.4, 'max': 2.4, 'title': 'eta', 'sel': 'tau_genpt>0&&tau_pt>0'},

    'tau_flightLength': {'var': 'tau_flightLength', 'nbin': 50, 'min': 0., 'max': 0.1, 'title': 'tau_flightLength', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_flightLength>=0'},
    'tau_flightLength_sig': {'var': 'tau_flightLength_sig', 'nbin': 25, 'min': 0., 'max': 5, 'title': 'tau_flightLength_sig', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_flightLength>=0'},

    'tau_ip3d': {'var': 'tau_ip3d', 'nbin': 50, 'min': 0., 'max': 0.1, 'title': 'tau_ipd3', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'tau_ip3d_err': {'var': 'tau_ip3d_err', 'nbin': 40, 'min': 0., 'max': 0.02, 'title': 'tau_ip3d_err', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'tau_ip3d_sig': {'var': 'tau_ip3d_sig', 'nbin': 25, 'min': 0., 'max': 5, 'title': 'tau_ip3d_sig', 'sel': 'tau_genpt>0&&tau_pt>0'},

    'tau_mass_1prong': {'var': 'tau_mass', 'nbin': 30, 'min': 0., 'max': 2.5, 'title': 'Tau mass, 1prong', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_dm==0'},
    'tau_mass_1prongp0': {'var': 'tau_mass', 'nbin': 30, 'min': 0., 'max': 2.5, 'title': 'Tau mass, 1prong+#pi^{0}', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_dm==1'},
    'tau_mass_2prong': {'var': 'tau_mass', 'nbin': 30, 'min': 0., 'max': 2.5, 'title': 'Tau mass, 2prong', 'sel': 'tau_genpt>0&&tau_pt>0&&(tau_dm==5 || tau_dm==6)'},
    'tau_mass_3prong': {'var': 'tau_mass', 'nbin': 30, 'min': 0., 'max': 2.5, 'title': 'Tau mass, 3prong (+#pi^{0})', 'sel': 'tau_genpt>0&&tau_pt>0&&(tau_dm==10 || tau_dm==11)'},
    'tau_mass_3prong_old': {'var': 'tau_mass', 'nbin': 30, 'min': 0., 'max': 2.5, 'title': 'Tau mass, 3prong (0#pi^{0})', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_dm==10'},

    'tau_mass_oldDM': {'var': 'tau_mass', 'nbin': 30, 'min': 0., 'max': 2.5, 'title': 'Tau mass (oldDMs)', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_decayModeFinding > 0.5'},

    'tau_phi': {'var': 'tau_phi', 'nbin': 16, 'min': -3.2, 'max': 3.2, 'title': 'phi', 'sel': 'tau_genpt>0&&tau_pt>0'},
    'tau_pt': {'var': 'tau_pt', 'nbin': 24, 'min': 0., 'max': 120, 'title': 'p_T [GeV]', 'sel': 'tau_genpt>0&&tau_pt>0'},


    # These plots will only be made for samples with genuine tau's like ZTT (because gen info is needed)
    'pt_resolution_1prong': {'var': '(tau_genpt-tau_pt)/(tau_genpt)', 'nbin': 30, 'min': -1., 'max': 1., 'title': 'pT resolution, 1prong',           'sel': 'tau_genpt>0&&tau_pt>0&&tau_dm==0'},
    'pt_resolution_1prongp0': {'var': '(tau_genpt-tau_pt)/(tau_genpt)', 'nbin': 30, 'min': -1., 'max': 1., 'title': 'pT resolution, 1prong+#pi^{0}', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_dm==1'},
    'pt_resolution_2prong': {'var': '(tau_genpt-tau_pt)/(tau_genpt)', 'nbin': 30, 'min': -1., 'max': 1., 'title': 'pT resolution, 2prong',           'sel': 'tau_genpt>0&&tau_pt>0&&(tau_dm==5 || tau_dm==6)'},
    'pt_resolution_3prong': {'var': '(tau_genpt-tau_pt)/(tau_genpt)', 'nbin': 30, 'min': -1., 'max': 1., 'title': 'pT resolution, 3prong (+#pi^{0})', 'sel': 'tau_genpt>0&&tau_pt>0&&(tau_dm==10 || tau_dm==11)'},
    'pt_resolution_3prong_old': {'var': '(tau_genpt-tau_pt)/(tau_genpt)', 'nbin': 30, 'min': -1., 'max': 1., 'title': 'pT resolution, 3prong (0#pi^{0})', 'sel': 'tau_genpt>0&&tau_pt>0&&tau_dm==10'},


    # Does not exist as branch in rel val samples anymore    
    # 'tau_MVAIsoRaw17v2': {'var': 'tau_byIsolationMVArun2017v2DBoldDMwLTraw2017', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    # 'tau_MVAIsoRaw17v1': {'var': 'tau_byIsolationMVArun2017v1DBoldDMwLTraw2017', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    # 'tau_MVAIsoRaw16': {'var': 'tau_byIsolationMVArun2v1DBoldDMwLTraw2016', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    # 'tau_MVAIsoRaw16new': {'var': 'tau_byIsolationMVArun2v1DBnewDMwLTraw2016', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (newDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFindingNewDMs > 0.5'},
    # 'tau_MVAIsoRaw17v2dR0p3': {'var': 'tau_byIsolationMVArun2017v2DBoldDMdR0p3wLTraw2017', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},
    # 'tau_MVA17v2': {'var': 'tau_byIsolationMVArun2017v2DBoldDMwLTraw2017', 'nbin': 40, 'min': -1., 'max': 1, 'title': 'Raw IsoMVA (oldDMs)', 'sel': 'tau_genpt > 0 && tau_pt > 0 && tau_decayModeFinding > 0.5'},


    #'charged_isoPt02':{'var':'tau_iso_dz02', 'nbin':20, 'min':0., 'max':10, 'title':'charged iso (|dz|<0.2cm) [GeV]', 'sel':'tau_genpt>0&&tau_pt>0'},
    #'charged_isoPt01':{'var':'tau_iso_dz02', 'nbin':20, 'min':0., 'max':10, 'title':'charged iso (|dz|<0.1cm) [GeV]', 'sel':'tau_genpt>0&&tau_pt>0'},
    #'charged_isoPt001':{'var':'tau_iso_dz001', 'nbin':20, 'min':0., 'max':10, 'title':'charged iso (|dz|<0.015cm) [GeV]', 'sel':'tau_genpt>0&&tau_pt>0'},
    #'charged_isoPt003':{'var':'tau_iso_dz001', 'nbin':20, 'min':0., 'max':10, 'title':'charged iso (|dz|<0.03cm) [GeV]', 'sel':'tau_genpt>0&&tau_pt>0'},

    

    
}
