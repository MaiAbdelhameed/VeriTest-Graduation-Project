import Image from "next/image";
import Link from "next/link";
export default function Navbar_component() {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">
          VeriTest
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <Link className="nav-link" href={"/"}>
              Home
            </Link>

            <Link className="nav-link" href={"/mode1"}>
              Mode 1
            </Link>

            <Link className="nav-link" href={"/mode2"}>
              Mode 2
            </Link>
            <Link className="nav-link" href={"/mode3"}>
              Mode 3
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
