# Generated by rust2rpm 24
%bcond_with check
%global debug_package %{nil}

%global crate axum

Name:           rust-axum
Version:        0.6.20
Release:        %{autorelease}.rv64_nc
Summary:        Web framework that focuses on ergonomics and modularity

License:        MIT
URL:            https://crates.io/crates/axum
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove documentation-specific feature
Patch:          axum-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Web framework that focuses on ergonomics and modularity.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+form-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+form-devel %{_description}

This package contains library source intended for building other packages which
use the "form" feature of the "%{crate}" crate.

%files       -n %{name}+form-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+headers-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+headers-devel %{_description}

This package contains library source intended for building other packages which
use the "headers" feature of the "%{crate}" crate.

%files       -n %{name}+headers-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http1-devel %{_description}

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%files       -n %{name}+http1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+matched-path-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+matched-path-devel %{_description}

This package contains library source intended for building other packages which
use the "matched-path" feature of the "%{crate}" crate.

%files       -n %{name}+matched-path-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+multipart-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multipart-devel %{_description}

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%files       -n %{name}+multipart-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+original-uri-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+original-uri-devel %{_description}

This package contains library source intended for building other packages which
use the "original-uri" feature of the "%{crate}" crate.

%files       -n %{name}+original-uri-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+query-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+query-devel %{_description}

This package contains library source intended for building other packages which
use the "query" feature of the "%{crate}" crate.

%files       -n %{name}+query-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tower-http-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tower-http-devel %{_description}

This package contains library source intended for building other packages which
use the "tower-http" feature of the "%{crate}" crate.

%files       -n %{name}+tower-http-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tower-log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tower-log-devel %{_description}

This package contains library source intended for building other packages which
use the "tower-log" feature of the "%{crate}" crate.

%files       -n %{name}+tower-log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ws-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ws-devel %{_description}

This package contains library source intended for building other packages which
use the "ws" feature of the "%{crate}" crate.

%files       -n %{name}+ws-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
