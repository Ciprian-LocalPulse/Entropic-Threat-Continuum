from simulation import ETCFramework, SecurityState, ThreatAction, contextual_exposure, etc_security_functional


def test_security_functional_rewards_balanced_states():
    balanced = etc_security_functional(SecurityState(0.8, 0.8, 0.8))
    unbalanced = etc_security_functional(SecurityState(1.0, 0.4, 1.0))
    assert balanced > unbalanced


def test_transition_degrades_weighted_axis():
    framework = ETCFramework(SecurityState(1.0, 1.0, 1.0))
    next_state = framework.transition(ThreatAction("phishing", {"AIA": 1.0}, effort=4, impact=0.5))
    assert next_state.aia < next_state.cea
    assert next_state.aia < next_state.ica


def test_contextual_exposure_increases_with_audience():
    small = contextual_exposure(1.0, audience_size=10, sensitivity=0.8)
    large = contextual_exposure(1.0, audience_size=10000, sensitivity=0.8)
    assert large > small
