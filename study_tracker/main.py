# 3️⃣ Partial Guidance Exercise
from tracker import add_study_hours, calculate_total_hours, build_dict, average
from report import print_study_summary

def main():
    study = {

    }
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    track = build_dict(study, days)
    new_track = add_study_hours(track, "Monday",9)
    new_track = add_study_hours(track, "Sunday", 4)
    new_track = add_study_hours(track,"Saturday",15)

    total = calculate_total_hours(new_track)
    averages = total/len(new_track)
    print_study_summary(total, averages)


if __name__ == "__main__":
    main()