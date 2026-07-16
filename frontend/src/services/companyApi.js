export async function fetchCompany(companyId) {
  const response = await fetch(
    `http://127.0.0.1:5000/api/company/${companyId}`
  );

  if (!response.ok) {
    throw new Error("API Error");
  }

  return response.json();
}
