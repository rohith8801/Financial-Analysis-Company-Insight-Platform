function SkeletonCard() {
  return (
    <div className="bg-white/80 rounded-2xl p-8 shadow-xl animate-pulse">
      <div className="h-6 bg-gray-300 rounded w-1/3 mb-4"></div>

      <div className="grid grid-cols-3 gap-6 mt-6">
        <div className="h-20 bg-gray-200 rounded"></div>
        <div className="h-20 bg-gray-200 rounded"></div>
        <div className="h-20 bg-gray-200 rounded"></div>
      </div>

      <div className="mt-8 grid grid-cols-2 gap-6">
        <div className="h-24 bg-gray-200 rounded"></div>
        <div className="h-24 bg-gray-200 rounded"></div>
      </div>
    </div>
  );
}

export default SkeletonCard;
