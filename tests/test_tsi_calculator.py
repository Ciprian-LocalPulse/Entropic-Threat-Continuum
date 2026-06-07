from simulation.tsi_calculator import AttackVector, ThreatSurfaceIntegral


def test_tsi_reports_axis_totals_and_top_vectors():
    tsi = ThreatSurfaceIntegral(
        [
            AttackVector("CEA-L-01", "CEA", 0.5, 0.5, 0.5),
            AttackVector("AIA-L-01", "AIA", 1.0, 0.8, 0.9),
        ]
    )
    report = tsi.report()
    assert report["total_exposure"] > 0
    assert report["axis_totals"]["AIA"] > report["axis_totals"]["CEA"]
    assert report["top_vectors"][0]["code"] == "AIA-L-01"
