all_tau_ids = [
    ('byCombinedIsolationDeltaBetaCorrRaw3Hits', float),
    ('byLooseCombinedIsolationDeltaBetaCorr3Hits', int),
    ('byMediumCombinedIsolationDeltaBetaCorr3Hits', int),
    ('byTightCombinedIsolationDeltaBetaCorr3Hits', int),
    ('byIsolationMVArun2v1DBoldDMwLTraw', float),
    ('byVLooseIsolationMVArun2v1DBoldDMwLT', int),
    ('byLooseIsolationMVArun2v1DBoldDMwLT', int),
    ('byMediumIsolationMVArun2v1DBoldDMwLT', int),
    ('byTightIsolationMVArun2v1DBoldDMwLT', int),
    ('byVTightIsolationMVArun2v1DBoldDMwLT', int),
    ('byVVTightIsolationMVArun2v1DBoldDMwLT', int),
    ('byIsolationMVArun2v1PWoldDMwLTraw', float),
    ('byLooseIsolationMVArun2v1PWoldDMwLT', int),
    ('byMediumIsolationMVArun2v1PWoldDMwLT', int),
    ('byTightIsolationMVArun2v1PWoldDMwLT', int),
    ('byVLooseIsolationMVArun2v1PWoldDMwLT', int),
    ('byVTightIsolationMVArun2v1PWoldDMwLT', int),
    ('byVVTightIsolationMVArun2v1PWoldDMwLT', int),
    ('byIsolationMVArun2v1DBdR03oldDMwLTraw', float),
    ('byLooseIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byMediumIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byTightIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byVLooseIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byVTightIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('byVVTightIsolationMVArun2v1DBdR03oldDMwLT', int),
    ('chargedIsoPtSum', float),
    ('neutralIsoPtSum', float),
    ('puCorrPtSum', float),
    ('neutralIsoPtSumWeight', float),
    ('footprintCorrection', float),
    ('photonPtSumOutsideSignalCone', float),
    ('decayModeFinding', int),
    ('decayModeFindingNewDMs', int),
    # # deepTauIDv2 vs jet discriminator
    # ("byDeepTau2017v2VSjetraw", float),
    # ("byVVVLooseDeepTau2017v2VSjet", int),
    # ("byVVLooseDeepTau2017v2VSjet", int),
    # ("byVLooseDeepTau2017v2VSjet", int),
    # ("byLooseDeepTau2017v2VSjet", int),
    # ("byMediumDeepTau2017v2VSjet", int),
    # ("byTightDeepTau2017v2VSjet", int),
    # ("byVTightDeepTau2017v2VSjet", int),
    # ("byVVTightDeepTau2017v2VSjet", int),
    # # deepTauIDv2 vs electron discriminator
    # ("byDeepTau2017v2VSeraw", float),
    # ("byVVVLooseDeepTau2017v2VSe", int),
    # ("byVVLooseDeepTau2017v2VSe", int),
    # ("byVLooseDeepTau2017v2VSe", int),
    # ("byLooseDeepTau2017v2VSe", int),
    # ("byMediumDeepTau2017v2VSe", int),
    # ("byTightDeepTau2017v2VSe", int),
    # ("byVTightDeepTau2017v2VSe", int),
    # ("byVVTightDeepTau2017v2VSe", int),
    # # deepTauIDv2 vs muon discriminator
    # ("byDeepTau2017v2VSmuraw", float),
    # ("byVLooseDeepTau2017v2VSmu", int),
    # ("byLooseDeepTau2017v2VSmu", int),
    # ("byMediumDeepTau2017v2VSmu", int),
    # ("byTightDeepTau2017v2VSmu", int),


]

lepton_tau_ids = [
    ('againstMuonLoose3', int),
    ('againstMuonTight3', int),
    ('againstElectronVLooseMVA6', int),
    ('againstElectronLooseMVA6', int),
    ('againstElectronMediumMVA6', int),
    ('againstElectronTightMVA6', int),
    ('againstElectronVTightMVA6', int),
    ('againstElectronMVA6Raw', float),
]

all_wps = ['VVVLoose','VVLoose', 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight']

def create_tau_ids(name, n_wps=7):
    # old when there were less WPs
    # wps = all_wps[:]
    # if n_wps == 6:
    #     wps = all_wps[1:]
    # if n_wps == 5:
    #     wps = all_wps[1:6]


    if n_wps == 4:
        wps = all_wps[2:6]
    elif n_wps == 6:
        wps = all_wps[2:]
    elif n_wps == 7:
        wps = all_wps[1:]
    elif n_wps == 8:
        wps = all_wps[:]


    return [('by' + wp + name, int) for wp in wps] + ['by' + name[:-4] + 'raw' + name[-4:]]


tau_ids = {
    # 'deepTauIDv2VSe':create_tau_ids(name='DeepTau2017v2VSe2017',n_wps=4),
    # 'deepTauIDv2VSmu':create_tau_ids(name='DeepTau2017v2VSmu2017',n_wps=8),
    # 'deepTauIDv2VSjet':create_tau_ids(name='DeepTau2017v2VSjet2017',n_wps=8),
    '2017v2':create_tau_ids('IsolationMVArun2017v2DBoldDMwLT2017'),
    '2017v1':create_tau_ids('IsolationMVArun2017v1DBoldDMwLT2017'),
    '2016v1':create_tau_ids('IsolationMVArun2v1DBoldDMwLT2016', 6),
    'newDM2016v1':create_tau_ids('IsolationMVArun2v1DBnewDMwLT2016', 6),
    'dR0p32017v2':create_tau_ids('IsolationMVArun2017v2DBoldDMdR0p3wLT2017')
}

def fill_tau_ids(avd, tau, tau_id_names):
    for (tau_id, _) in tau_id_names:
        avd['tau_'+tau_id].fill(tau.tauID(tau_id))
