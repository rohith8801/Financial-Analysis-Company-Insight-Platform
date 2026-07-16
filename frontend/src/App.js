import CompanyList from "./pages/CompanyList";

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-gray-100 to-slate-200">
      {/* Header */}
      <header className="sticky top-0 z-50 backdrop-blur bg-white/70 border-b border-gray-200">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-extrabold tracking-tight text-gray-800">
            Bluestock
            <span className="text-blue-600">.</span>
          </h1>
          <span className="text-sm text-gray-500">
            Financial Insights Dashboard
          </span>
        </div>
      </header>

      {/* Main */}
      <main className="pb-16">
        <CompanyList />
      </main>
    </div>
  );
}

export default App;
