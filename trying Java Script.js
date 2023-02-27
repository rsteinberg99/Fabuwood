function delivery() {
   const small_pack = parseInt(document.getElementById("small-packages").value);
   const med_pack = parseInt(document.getElementById("medium-packages").value);
   const large_pack = parseInt(document.getElementById("large-packages").value);

   if (validation(small_pack, med_pack, large_pack)) {
      alert("The amount of packages you entered is larger than the truck's capacity. Please input the amount of packages again.");
   }
}

function calculation() {
   const driving_time = parseFloat(document.getElementById("driving-time").value);
   const distance = parseFloat(document.getElementById("distance").value);

   if (driving_time <= 0 || distance <= 0) {
      alert("Invalid input.");
   } else {
      const total_pay_per_route = drivers_salary_hr * driving_time;
      const total_gallons = distance / 6.5;
      const total_gas_expense = gas_price;}