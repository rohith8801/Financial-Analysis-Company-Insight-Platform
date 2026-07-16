import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { loadCompany } from "../redux/companySlice";
import SkeletonCard from "../components/skeletonCard";


function CompanyList() {
  const [companyId, setCompanyId] = useState("");
  const dispatch = useDispatch();
  const { companies, loading, error } = useSelector(
    (state) => state.company
  );

  const handleSearch = () => {
    if (companyId.trim() !== "") {
      dispatch(loadCompany(companyId.toUpperCase()));
    }
  };

  return (
  <div className="max-w-6xl mx-auto mt-12 px-6">
    {/* Search */}
    <div className="flex flex-col sm:flex-row gap-3 mb-10">
      <input
        type="text"
        placeholder="Search company (e.g. BAJAJ-AUTO)"
        value={companyId}
        onChange={(e) => setCompanyId(e.target.value)}
        className="flex-1 px-4 py-3 rounded-xl border border-gray-300 
                   focus:ring-2 focus:ring-blue-500 focus:outline-none
                   shadow-sm transition"
      />
      <button
        onClick={handleSearch}
        className="px-6 py-3 rounded-xl bg-blue-600 text-white font-semibold
                   hover:bg-blue-700 active:scale-95 transition-all
                   shadow-lg"
      >
        Analyze
      </button>
    </div>

    {/* States */}
    {loading && (
      <div className="text-center text-gray-600 animate-pulse">
        Analyzing financials...
      </div>
    )}

    {error && (
      <div className="text-center text-red-500 bg-red-50 p-4 rounded-xl">
        Unable to fetch data. Please check the company ID.
      </div>
    )}

    {loading && (
  <div className="mt-10">
    <SkeletonCard />
  </div>
)}


    {/* Company Card */}
    {companies.map((c) => (
      <div
        key={c.id}
        className="bg-white/80 backdrop-blur-xl rounded-2xl p-8 mt-8
                   shadow-xl hover:shadow-2xl transition-all duration-300"
      >
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <h2 className="text-3xl font-bold text-gray-800">
            {c.name}
          </h2>
          <span className="px-4 py-1 rounded-full bg-blue-100 text-blue-700 text-sm font-semibold">
            {c.id}
          </span>
        </div>

        {/* Metrics */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-6">
          <Metric title="ROE" value={`${c.roe}%`} />
          <Metric title="ROCE" value={`${c.roce}%`} />
          <Metric title="Net Profit" value={c.net_profit} />
        </div>

        {/* Pros & Cons */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
          <InsightBlock
            title="Pros"
            color="green"
            items={c.pros}
          />
          <InsightBlock
            title="Cons"
            color="red"
            items={c.cons}
          />
        </div>
      </div>
    ))}
  </div>
);

}

export default CompanyList;
function Metric({ title, value }) {
  return (
    <div className="bg-white rounded-xl p-5 shadow-md text-center">
      <p className="text-sm text-gray-500">{title}</p>
      <p className="text-2xl font-bold text-gray-800 mt-1">
        {value}
      </p>
    </div>
  );
}

function InsightBlock({ title, color, items }) {
  const styles =
    color === "green"
      ? "bg-green-50 text-green-700"
      : "bg-red-50 text-red-700";

  return (
    <div className={`rounded-xl p-5 ${styles}`}>
      <h3 className="font-semibold mb-3">{title}</h3>
      <div className="flex flex-wrap gap-2">
        {items.map((item, i) => (
          <span
            key={i}
            className="px-3 py-1 bg-white/70 rounded-full text-sm shadow-sm"
          >
            {item}
          </span>
        ))}
      </div>
    </div>
  );
}
