import networkx as nx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.entities import DependencyEdge


async def build_graph(db: AsyncSession) -> nx.DiGraph:
    graph = nx.DiGraph()
    edges = await db.scalars(select(DependencyEdge))
    for edge in edges:
        graph.add_edge(edge.depends_on_asset_id, edge.source_asset_id)
    return graph


async def restore_order(db: AsyncSession, target_assets: list[int]) -> list[int]:
    graph = await build_graph(db)
    ordered = list(nx.topological_sort(graph)) if graph.nodes else []
    for target in target_assets:
        if target not in ordered:
            ordered.append(target)
    return [node for node in ordered if node in target_assets]
