class Reach:
    def __init__(self, fb, yt, google, insta) -> None:
        self.actual_reach_mapper = {
            0: "0K",
            1: "1K",
            2: "5K",
            3: "10K",
            4: "50K",
            5: "0.1M",
            6: "0.5M",
            7: "1M",
        }

        self.fb_reach_mapper = {
            0: 0,
            1: 700,
            2: 14000,
            3: 35000,
            4: 105000,
            5: 560000,
            6: 840000,
            7: 1050000,
        }

        self.insta_reach_mapper = {
            0: 0,
            1: 840,
            2: 60000,
            3: 120000,
            4: 600000,
            5: 2400000,
            6: 3000000,
            7: 4500000,
        }

        self.yt_reach_mapper = {
            0: 0,
            1: 800,
            2: 30000,
            3: 70000,
            4: 400000,
            5: 1200000,
            6: 1800000,
            7: 2500000,
        }

        self.google_reach_mapper = {
            0: 0,
            1: 790,
            2: 50000,
            3: 90000,
            4: 500000,
            5: 1800000,
            6: 2200000,
            7: 3500000,
        }

        self.fb = fb
        self.yt = yt
        self.google = google
        self.insta = insta

    def amount_calculation(self):
        try:
            return {
                "fbCost": self.fb_reach_mapper[self.fb],
                "ytCost": self.yt_reach_mapper[self.yt],
                "googleCost": self.google_reach_mapper[self.google],
                "instaCost": self.insta_reach_mapper[self.insta],
                "totalCost": self.fb_reach_mapper[self.fb]
                + self.yt_reach_mapper[self.yt]
                + self.google_reach_mapper[self.google]
                + self.insta_reach_mapper[self.insta],
            }

        except Exception as e:
            print(f"Reach calculation failed due to {e}")
            return {}

    def actual_reach(self):
        try:
            return {
                "fbReach": self.actual_reach_mapper[self.fb],
                "ytReach": self.actual_reach_mapper[self.yt],
                "googleReach": self.actual_reach_mapper[self.google],
                "instaReach": self.actual_reach_mapper[self.insta],
            }
        except Exception as e:
            print(f"Reach mapping to actual values failed due to {e} ")
            return {}
