export default function Header({ onClick }) {
  return (
    <header className="app-header">
      <div className="header-inner">
        <span className="app-logo" onClick={onClick}>
          FeedChef
        </span>
      </div>
    </header>
  );
}