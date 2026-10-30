def run_dosage_calculator():
    history = []
    print("===== Medication Dosage Calculator =====")
    while True:
        user_input = input("Enter prescribed dose in mg/kg (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        try:
            dose_per_kg = float(user_input)
            if dose_per_kg <= 0:
                raise ValueError("Prescribed dose must be greater than zero")
            weight = float(input("Enter patient weight in kg: "))
            if weight <= 0:
                raise ValueError("Patient weight must be greater than zero")
            mg_per_tablet = float(input("Enter mg per tablet: "))
            if mg_per_tablet <= 0:
                raise ValueError("Tablet strength must be greater than zero")
            total_dose = dose_per_kg * weight
            tablets = total_dose / mg_per_tablet
        except ValueError as e:
            print(f"ValueError: {e}")
            history.append(("fail", str(e)))
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
            history.append(("fail", str(e)))
        else:
            print(f"Total dose: {total_dose:.2f} mg | Tablets needed: {tablets:.2f}")
            description_str = f"{dose_per_kg} mg/kg / {weight} kg / {mg_per_tablet} mg tab"
            history.append(("success", description_str))
        finally:
            print("---")
    return history
run_dosage_ca